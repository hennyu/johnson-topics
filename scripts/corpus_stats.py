#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import PlaintextCorpusReader
import plotly.graph_objects as go
import pandas as pd
from os.path import join
from plotly.subplots import make_subplots
import re




def get_corpus_statistics():
	"""
	get basic corpus statistics
	"""
	corpus_tokens = len(corpus.words())
	corpus_types = len(set(corpus.words()))
	ttr = corpus_types / corpus_tokens
	print("tokens: " + str(corpus_tokens))
	print("types: " + str(corpus_types))
	print("ttr: " + str(ttr))
	
	
	
def plot_document_lengths():
	"""
	plot the lengths of the documents in the corpus
	and write the lengths to a csv file
	"""
	
	file_lens = []
	for corpus_file in corpus.fileids():
		file_content = corpus.words(corpus_file)
		file_len = len(file_content)
		file_lens.append(file_len)

	lens_frame = pd.DataFrame(columns=["id", "tokens"])
	lens_frame["id"] = corpus.fileids()
	lens_frame["tokens"] = file_lens
	lens_frame.to_csv(join(wdir, "data", "tokens.csv"))

	y = file_lens
	
	fig = go.Figure()
	fig.add_trace(go.Box(y=y, name="documents"))
	fig.update_layout(width=400,height=600)
	fig.update_yaxes(title="number of tokens",exponentformat="none")

	fig.show()
	

def plot_sender_receiver_statistics(sr):
	"""
	plot the top ten senders/receivers of letters
	
	sr (str): "sender" or "receiver"
	"""

	# read metadata
	md = pd.read_csv(join(wdir, md_filepath), sep=",", index_col=0, header=0)

	# sender/receiver
	srg = md.groupby(by=sr).size().sort_values(ascending=False)
	senders_receivers_num = len(srg)
	print("number of " + sr + "s: " + str(senders_receivers_num))
	srg_top_ten = srg[0:10]
	srg_top_ten_sum = sum(list(srg_top_ten))
	print("number of letters by top ten " + sr + "s: " + str(srg_top_ten_sum) + " (" + str(srg_top_ten_sum / len(md)) + "%)")

	x_labels = list(srg_top_ten.index)
	x_labels_space = [re.sub("([A-Z])"," \g<0>",x) for x in x_labels]

	y_values = list(srg_top_ten)
	y_values_rel = [y / len(md) for y in y_values]

	fig = make_subplots(specs=[[{"secondary_y": True}]])

	fig.add_trace(
		go.Bar(x=x_labels_space, y=y_values, name="y_axis_1"),
		secondary_y=False,
	),
	fig.add_trace(
		go.Bar(x=x_labels_space, y=y_values_rel, name="y_axis_2"),
		secondary_y=True,
	)


	fig.update_layout(width=400,height=800,showlegend=False,margin=dict(l=20, r=20, t=20, b=500),font=dict(size=18),autosize=False)
	fig.update_xaxes(tickangle=270, title=sr+" name(s)", automargin=False)
	fig.update_yaxes(title="number of letters (absolute)", secondary_y=False, range=[0, 650])
	fig.update_yaxes(title="number of letters (relative)", secondary_y=True, range=[0,650/len(md)])
	fig.show()



#####################################
	
corpus_root = "/home/ulrike/Git/johnson-topics/data/letters-leipzig-txt"
corpus = PlaintextCorpusReader(corpus_root, '.*')
wdir = "/home/ulrike/Git/johnson-topics"
md_filepath = "data/letters-leipzig-metadata.csv"

#get_corpus_statistics()
plot_document_lengths()
#plot_sender_receiver_statistics("sender")
#plot_sender_receiver_statistics("receiver")

