# SingleLinkageClustering

This is an experiment of different implementations for the *Single Linkage Clustering* algorithm in order to improve its performance applying different optimizations.

## Set up

Before to start with the implementation, we will describe what the project needs to run correctly.

### Dependencies

Although the project has been though to run without external implementations, we have used the matplotlib package to perform the plots.

This is a Python 3.6 project and uses the [Pipenv](https://docs.pipenv.org/) utility recommended by Python to manage the dependencies of the project. This tool's very easy of [install](https://docs.pipenv.org/#install-pipenv-today) and [use](https://docs.pipenv.org/basics/#environment-management-with-pipenv) it, and allows to build a Python work environment using the *Pipfile* and *Pipfile.lock* files included on the repository.

### Executions

On the repository, we have included 3 ways of executing the algorithm: test, run_example, and run_timing:

#### Test

Allows to run some simple test to check that all the version works correctly:
```
python tests.py
```

#### Run example

Allows running a simple example to test how the algorithm works. At the file start, we can configure some parameters to tune the execution. Finally, this execution produces a plot with the final clustering.
```
python run_example.py
```

#### Run timing

Allows running a timing comparison between the 4 implemented versions. At the file start, we can configure some parameters to tune the executions. Finally, this execution produces a plot with the final timing comparison.
```
python run_timing.py
```

## Implementation

## Comparision

## Conclusions and future work

## References

1. [Single-linkage clustering](https://en.wikipedia.org/wiki/Single-linkage_clustering)
2. [Single Linkage Clustering Quiz - Georgia Tech - Machine Learning](https://www.youtube.com/watch?v=HfikjFVM3dg)
3. [E2LSH 0.1: User Manual](http://www.mit.edu/~andoni/LSH/manual.pdf)
4. [Nearest-Neighbor Methods in Learning and Vision: Theory and Practice - Introduction](http://people.csail.mit.edu/gregory/annbook/introduction.pdf)
