"""
Reading comprehension is loosely defined as follows: given a question and a passage of text that
contains the answer, answer the question.

These submodules contain models for things that are predominantly focused on reading comprehension.
"""

from allennlp.models.reading_comprehension.bidaf import BidirectionalAttentionFlow
from allennlp.models.reading_comprehension.bidaf_ensemble import BidafEnsemble
from allennlp.models.reading_comprehension.dialog_qa import DialogQA
from allennlp.models.reading_comprehension.naqanet import NumericallyAugmentedQaNet
from allennlp.models.reading_comprehension.qanet import QaNet
from allennlp.models.reading_comprehension.qanet_fine_grained import QaNet_fine_grained
from allennlp.models.reading_comprehension.qanet_fine_grained3 import QaNet_fine_grained3
from allennlp.models.reading_comprehension.qanet_pure_fine import QaNet_pure_fine