#!/usr/bin/env python3
"""
Scrape authentic public daily contribution counts from GitHub's contributions endpoint
and write data/contributions.json with raw days and derived statistics.

No auth token or GraphQL required — scrapes the public HTML endpoint served by GitHub.
Designed to run in GitHub Actions on a daily schedule.
"""
import datetime
import json
import os
import re
import sys
import requests
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
USERNAME = os.environ.get("GH_PROFILE_USER", "Ritik-62")
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_PATH = os.path.join(HERE, "..", "data", "contributions.json")


def fetch_days():
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; profile-readme-bot/1.0)",
        "Accept": "text/html,application/xhtml+xml",
    }
    resp = requests.get(URL, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    cells = soup.select("td.ContributionCalendar-day")
    if not cells:
        print(f"Warning: No calendar cells found for user {USERNAME}.", file=sys.stderr)
        return []

    days = []
    for td in cells:
        date = td.get("data-date")
        if not date:
            continue
        td_id = td.get("id")
        tooltip_el = soup.find("tool-tip", attrs={"for": td_id}) if td_id else None
        text = tooltip_el.get_text(strip=True) if tooltip_el else ""
        if re.search(r"no contributions", text, re.I):
            count = 0
        else:
            m = re.match(r"(\d+)", text)
            count = int(m.group(1)) if m else 0
        days.append({"date": date, "count": count, "level": int(td.get("data-level") or 0)})

    days.sort(key=lambda d: d["date"])
    return days


def compute_current_streak(days):
    if not days:
        return 0, None, None
    idx = len(days) - 1
    if days[idx]["count"] == 0:
        idx -= 1  # current day is still ongoing
    streak = 0
    end_idx = idx
    while idx >= 0 and days[idx]["count"] > 0:
        streak += 1
        idx -= 1
    start_idx = idx + 1
    if streak == 0 or start_idx > end_idx:
        return 0, None, None
    return streak, days[start_idx]["date"], days[end_idx]["date"]


def compute_longest_streak(days):
    if not days:
        return 0, None, None
    longest = run = 0
    longest_start = longest_end = None
    run_start_idx = None
    for i, d in enumerate(days):
        if d["count"] > 0:
            if run == 0:
                run_start_idx = i
            run += 1
            if run > longest:
                longest = run
                longest_start = days[run_start_idx]["date"]
                longest_end = days[i]["date"]
        else:
            run = 0
    return longest, longest_start, longest_end


def build_data(days):
    if not days:
        today_str = datetime.date.today().isoformat()
        return {
            "username": USERNAME,
            "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "range": {"start": today_str, "end": today_str},
            "total_contributions": 0,
            "active_days": 0,
            "avg_per_active_day": 0,
            "current_streak": {"length": 0, "start": None, "end": None},
            "longest_streak": {"length": 0, "start": None, "end": None},
            "best_day": {"date": today_str, "count": 0},
            "monthly": [],
            "days": [],
        }

    total = sum(d["count"] for d in days)
    active_days = sum(1 for d in days if d["count"] > 0)
    best = max(days, key=lambda d: d["count"])
    cur_len, cur_start, cur_end = compute_current_streak(days)
    long_len, long_start, long_end = compute_longest_streak(days)

    monthly = {}
    for d in days:
        key = d["date"][:7]
        monthly[key] = monthly.get(key, 0) + d["count"]
    monthly_list = [{"month": k, "total": v} for k, v in sorted(monthly.items())]

    return {
        "username": USERNAME,
        "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "range": {"start": days[0]["date"], "end": days[-1]["date"]},
        "total_contributions": total,
        "active_days": active_days,
        "avg_per_active_day": round(total / active_days, 1) if active_days else 0,
        "current_streak": {"length": cur_len, "start": cur_start, "end": cur_end},
        "longest_streak": {"length": long_len, "start": long_start, "end": long_end},
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": monthly_list,
        "days": days,
    }


if __name__ == "__main__":
    out_target = sys.argv[1] if len(sys.argv) > 1 else OUT_PATH
    days = fetch_days()
    data = build_data(days)
    os.makedirs(os.path.dirname(os.path.abspath(out_target)), exist_ok=True)
    with open(out_target, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {out_target}: {data['total_contributions']} contributions, "
          f"active days: {data['active_days']}, current streak: {data['current_streak']['length']}, "
          f"longest streak: {data['longest_streak']['length']}")
