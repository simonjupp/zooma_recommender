#!/usr/bin/env python
"""
Description goes here
"""
__author__ = "jupp"
__license__ = "Apache 2.0"
__date__ = "03/10/2018"

from efficient_apriori import apriori


transactions = [('OriginTissue : Blood', 'TumorType : Primary', 'SampleDiagnosis : acute myeloid leukemia', 'OriginTissue : Blood : UBERON_0000178'),
                ('OriginTissue : Blood', 'TumorType : Primary', 'SampleDiagnosis : acute myeloid leukemia','SampleDiagnosis : acute myeloid leukemia : NCIT_C3171'),
                ('OriginTissue : Blood', 'TumorType : Primary', 'SampleDiagnosis : acute myeloid leukemia', 'TumorType : Primary : UBERON_0002371')
                ,
                ('OriginTissue : Blood', 'TumorType : Metastatic', 'SampleDiagnosis : acute myeloid leukemia', 'OriginTissue : Blood : UBERON_0000178'),
                ('OriginTissue : Blood', 'TumorType : Metastatic', 'SampleDiagnosis : acute myeloid leukemia', 'SampleDiagnosis : Metastatic acute myeloid leukemia : EFO_00002'),
                ('OriginTissue : Blood', 'TumorType : Metastatic', 'SampleDiagnosis : acute myeloid leukemia', 'TumorType : Primary : ONTO_XXXX')

                ]
itemsets, rules = apriori(transactions, min_support=0,  min_confidence=0)

# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 3 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
    if "_" in rule.rhs[0]:
      print(rule) # Prints the rule and its confidence, support, lift, ...
