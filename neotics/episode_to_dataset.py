"""Turn a Neotics Episode into a LeRobot dataset, ready to train on.

    python episode_to_dataset.py samples/depot.episode.json out_dir

The measured joint positions become observation.state and the commanded positions become action.
"""
import sys

import numpy as np
from lerobot.datasets.lerobot_dataset import LeRobotDataset

from neotics_scene import load_episode

TASK = "Reach from home and return"


def convert(episode: dict, root: str, repo_id: str = "neotics/depot") -> LeRobotDataset:
    feature = {"dtype": "float32", "shape": (len(episode["joints"]),), "names": episode["joints"]}
    dataset = LeRobotDataset.create(
        repo_id=repo_id,
        fps=episode["rate_hz"],
        root=root,
        robot_type="neotics_arm",
        features={"observation.state": feature, "action": feature},
        use_videos=False,
    )
    for qpos, ctrl in zip(episode["qpos"], episode["ctrl"]):
        dataset.add_frame({"observation.state": np.array(qpos, dtype=np.float32), "action": np.array(ctrl, dtype=np.float32), "task": TASK})
    dataset.save_episode()
    dataset.finalize()
    return dataset


if __name__ == "__main__":
    print(convert(load_episode(sys.argv[1]), sys.argv[2]))
