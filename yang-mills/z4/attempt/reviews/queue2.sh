#!/usr/bin/env bash
# Director Z4: launch queued workers, at most three running at once (CLAUDE.md, asynchronous work, rule 4).
# usage: queue.sh <worker> [<worker> ...]   (each launched with model opus, timeout 3000 s)
cd /home/user/z4-workers
for w in "$@"; do
  while [ "$(pgrep -fc 'launch2.sh ')" -ge 3 ]; do sleep 10; done
  nohup ./launch2.sh "$w" opus 3000 >/dev/null 2>&1 &
  echo "$(date -u +%H:%M:%S) launched $w" >> queue.log
  sleep 5
done
