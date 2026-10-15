#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""silent-failure-scanner — AI 静默失败扫描（占位/幻觉/空输出/无变化重复）。
理论根基：LGD 三律 + silent-failure-catalog 分类法。Usage:
  python silent_scanner.py <file|text> [--json]"""
import argparse, json, os, re, sys, hashlib

PATTERNS = {
    "placeholder": [r"(?i)TODO\s*[:：]", r"(?i)FIXME\s*[:：]", r"(?i)XXX\s*[:：]", r"(?i)lorem ipsum", r"待补充\s*[:：]", r"占位\s*[:：]", r"(?i)\{\{.*?\}\}"],
    "empty_or_stub": [r"(?i)^\s*(n/?a|tbd|待补|略|…)\.?\s*$"],
    "hedge_only": [r"(?i)^(maybe|perhaps|probably|应该|大概|或许)[^。.!?]{0,20}[。.!?]?\s*$"],
    "no_progress_repeat": [r"(?i)^(same as above|同上|和上面一样)$"],
    "hallucination_marker": [r"(?i)as of my last update|i don't have access to real-time", r"根据我的训练数据"],
    "contradiction": [r"(?i)(however|but)\s*,?\s*(opposite|contradict)", r"但是.*(矛盾|相反)"],
}

def scan(text):
    hits = []
    for cat, pats in PATTERNS.items():
        for p in pats:
            m = re.search(p, text, re.M)
            if m:
                hits.append({"category": cat, "pattern": p, "snippet": text[max(0, m.start()-15):m.end()+15]})
                break
    return hits

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="file path or text")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    if os.path.isfile(a.input):
        text = open(a.input, encoding="utf-8", errors="replace").read()
    else:
        text = a.input
    hits = scan(text)
    # 质量分：基线 100，每类命中 -20（fail-closed：检出即降级）
    score = max(0, 100 - len({h["category"] for h in hits}) * 20)
    verdict = "PASS" if score >= 80 else "FAIL"
    sha = hashlib.sha256(text.encode()).hexdigest()[:8]
    res = {"score": score, "verdict": verdict, "hits": hits, "sha256_8": sha,
           "note": "Static pattern scan; not a substitute for runtime verification"}
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"quality={score}/100 {verdict} (sha {sha})")
        for h in hits:
            print(f"  [HIT] {h['category']}: ...{h['snippet']}...")
    return 0 if verdict == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
