# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._iqtree2 import iqtree, iqtree_ultrafast_bootstrap
from ._version import get_versions
from ._align_to_tree_mafft_iqtree import align_to_tree_mafft_iqtree

__version__ = get_versions()['version']
del get_versions

__all__ = ["iqtree", "iqtree_ultrafast_bootstrap",
           "align_to_tree_mafft_iqtree"]
