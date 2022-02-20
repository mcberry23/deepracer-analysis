# deepracer-analysis

This is a set of notebooks and utilities to enable analysis of logs for AWS DeepRacer.

This is a fork of [aws-deepracer-community/deepracer-analysis](https://github.com/aws-deepracer-community/deepracer-analysis), [MickQG/deepracer-analysis](https://github.com/MickQG/deepracer-analysis), [cdthompson/deepracer-k1999-race-lines](https://github.com/cdthompson/deepracer-k1999-race-lines), and [TheRayG/deepracer-log-analysis](https://github.com/TheRayG/deepracer-log-analysis).

## Setup

The notebooks require Jupyter to run, together with deepracer-utils. While not needed
for using the notebooks, it's worth to also have Jupytext installed.

If you only plan to use the notebooks, I recommend that you make a copy of them to enable
seamless pulls of any updates.

If you pull latest changes for the notebooks, do also run
```
pip install --upgrade -r requirements.txt
```
in your venv. This way you will also get upgrades on the requirements.

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
jupyter lab
```

## Start Analysis

To run, simply start the juptyer notebook

```bash
jupyter notebook
```

## Notebook Descriptions
- `Racer-Line-Calculations`: Uses the K1999 algorithm to find the optimal path around the track
- `Track Analysis`: Creates a list of waypoints that can be passed to a reward function
- `DeepRacerLogAnalysis_Training`: Analyzes results of training logs
- `ActionSpace_analysis`: Finds the optimal action space for the corresponding track

## License
This project retains the license of the 
[aws-deepracer-workshops](https://github.com/aws-samples/aws-deepracer-workshops)
project which has been forked for the initial Community contributions.
Our understanding is that it is a license more permissive than the MIT license
and allows for removing of the copyright headers.

Unless clearly sated otherwise, this license applies to all files in this repository.

