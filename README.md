# deepracer-analysis

This is a set of notebooks and utilities to enable analysis of logs for AWS DeepRacer.

This is a fork of [aws-deepracer-community/deepracer-analysis](https://github.com/aws-deepracer-community/deepracer-analysis), [MickQG/deepracer-analysis](https://github.com/MickQG/deepracer-analysis), [cdthompson/deepracer-k1999-race-lines](https://github.com/cdthompson/deepracer-k1999-race-lines), and [TheRayG/deepracer-log-analysis](https://github.com/TheRayG/deepracer-log-analysis).

## Setup

Install pip packages
```
pip install --upgrade -r requirements.txt
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

