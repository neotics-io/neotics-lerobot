# Neotics kit for LeRobot

This folder is Neotics' own work, added to our copy of [LeRobot](https://github.com/huggingface/lerobot). It turns a recorded Neotics run into a LeRobot dataset, ready to train on.

It is one part of the Neotics stack. Every fork in [neotics-io](https://github.com/neotics-io) reads the same two files:

- a **Neotics Scene** (`samples/depot.scene.json`): the room, the obstacles, the arm and the named places;
- a **Neotics Episode** (`samples/depot.episode.json`): a run recorded in MuJoCo, with time, joint positions and commands.

The depot is a sample made for these tools. It is not an entry or an answer for any [Neotics challenge](https://lab.neotics.io).

## Use it

Run from this folder:

```bash
python episode_to_dataset.py samples/depot.episode.json out
```

## How it's checked

Installs this repository's LeRobot, converts the sample run, reopens the dataset and compares the numbers with the recording. This runs on GitHub in `.github/workflows/neotics.yml`, on every change to this folder.

## Licence

See [`LICENSE`](LICENSE). It covers this folder only.
