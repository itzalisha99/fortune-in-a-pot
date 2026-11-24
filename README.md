# Fortune in a Pot

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/itzalisha99/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/itzalisha99/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

A make.fun entry for **Fortune in a Pot**: one kind, funny fortune for a houseplant, 120 characters or fewer.

## The fortune

> Soon the windowsill will be yours alone, the cat has found a sunnier shelf, and the sun has chosen you.

## How it works

`main.py` (Python stdlib only, deterministic) writes the fortune to
`/output/entry.txt`. It validates the text against the bounty gate first:
1–120 characters, UTF-8, a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
