# -*- coding: utf-8 -*-

import pandas as pd

spam = pd.read_csv('./spam.csv')
spam.to_hdf('datasets.hdf','spam',complib='blosc',complevel=9)

