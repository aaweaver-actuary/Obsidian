
---
annotation-target::pdf/attention-is-all-you-need-2017.pdf
---

#transformers #bert #attention-is-all-you-need #nlp #rnn #neural-network

## 1. introduction

- before this paper the dominant models for language tasks:
    - #recurrent-neural-network ( #rnn )
    - #long-term-short-term-memory ( #lstm )
    - #gated-recurrent-neural-network

## 2. background

- current models [^1] use #cnn 's to simultaneously process inputs and outputs
    - "computing hidden representations in parallel for all input and output positions. "




>%%
>```annotation-json
>{"text":"These were considered state of the art when this paper was written","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":1380,"end":1474},{"type":"TextQuoteSelector","exact":"Recurrent neural networks, long short-term memory [12] and gated recurrent [7] neural networks","prefix":"om the literature.1 Introduction","suffix":"in particular, have been firmly"}]}],"created":"2023-08-22T23:34:01.900Z","updated":"2023-08-22T23:34:01.900Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf"}
>```
>%%
>*%%PREFIX%%om the literature.1 Introduction%%HIGHLIGHT%% ==Recurrent neural networks, long short-term memory [12] and gated recurrent [7] neural networks== %%POSTFIX%%in particular, have been firmly*
>%%LINK%%[[#^gu3zot3ecc|show annotation]]
>%%COMMENT%%
>These were considered state of the art when this paper was written
>%%TAGS%%
>#rnn, #lstm, #recurrent-neural-network, #gated-recurrent-neural-network, #long-term-short-term-memory
^gu3zot3ecc


>%%
>```annotation-json
>{"created":"2023-08-22T23:36:32.964Z","text":"Before transformer architecture, attention mechanisms were used with recurrent networks","updated":"2023-08-22T23:36:32.964Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":3839,"end":3951},{"type":"TextQuoteSelector","exact":"In all but a few cases [22], however, such attention mechanismsare used in conjunction with a recurrent network.","prefix":"ut or output sequences [2, 16]. ","suffix":"In this work we propose the Tran"}]}]}
>```
>%%
>*%%PREFIX%%ut or output sequences [2, 16].%%HIGHLIGHT%% ==In all but a few cases [22], however, such attention mechanismsare used in conjunction with a recurrent network.== %%POSTFIX%%In this work we propose the Tran*
>%%LINK%%[[#^6nek45ofwey|show annotation]]
>%%COMMENT%%
>Before transformer architecture, attention mechanisms were used with recurrent networks
>%%TAGS%%
> #transformer, #attention, #neural-network
^6nek45ofwey


>%%
>```annotation-json
>{"created":"2023-08-22T23:38:53.278Z","text":"recurrent models use the inherent structure","updated":"2023-08-22T23:38:53.278Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":2858,"end":2931},{"type":"TextQuoteSelector","exact":"Recurrent models typically factor computation along the symbol positions ","prefix":"NIPS 2017), Long Beach, CA, USA.","suffix":"of the input and outputsequences"}]}]}
>```
>%%
>*%%PREFIX%%NIPS 2017), Long Beach, CA, USA.%%HIGHLIGHT%% ==Recurrent models typically factor computation along the symbol positions== %%POSTFIX%%of the input and outputsequences*
>%%LINK%%[[#^pmgtq6ey4a|show annotation]]
>%%COMMENT%%
>recurrent models use the inherent structure
>%%TAGS%%
> #recurrent-neural-network, #rnn
^pmgtq6ey4a


>%%
>```annotation-json
>{"created":"2023-08-22T23:40:14.489Z","text":"cannot parallelize\n","updated":"2023-08-22T23:40:14.489Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":3141,"end":3225},{"type":"TextQuoteSelector","exact":"This inherentlysequential nature precludes parallelization within training examples,","prefix":"1 and the input for position t. ","suffix":" which becomes critical at longe"}]}]}
>```
>%%
>*%%PREFIX%%1 and the input for position t.%%HIGHLIGHT%% ==This inherentlysequential nature precludes parallelization within training examples,== %%POSTFIX%%which becomes critical at longe*
>%%LINK%%[[#^e2tcocyz64b|show annotation]]
>%%COMMENT%%
>cannot parallelize
>
>%%TAGS%%
>
^e2tcocyz64b


>%%
>```annotation-json
>{"created":"2023-08-22T23:42:41.330Z","text":"what is unique about transformer:\n\nthe first model relying completely on self-attention to represent inputs and outputs without sequence-aligned RNNs or convolution","updated":"2023-08-22T23:42:41.330Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":5806,"end":5989},{"type":"TextQuoteSelector","exact":"the Transformer is the first transduction model relyingentirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution","prefix":"best of our knowledge, however, ","suffix":". In the following sections, we "}]}]}
>```
>%%
>*%%PREFIX%%best of our knowledge, however,%%HIGHLIGHT%% ==the Transformer is the first transduction model relyingentirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution== %%POSTFIX%%. In the following sections, we*
>%%LINK%%[[#^qbky2zhmq0p|show annotation]]
>%%COMMENT%%
>what is unique about transformer:
>
>the first model relying completely on self-attention to represent inputs and outputs without sequence-aligned RNNs or convolution
>%%TAGS%%
>
^qbky2zhmq0p


>%%
>```annotation-json
>{"created":"2023-08-22T23:44:23.332Z","text":"most models like this use an encoder-decoder structure","updated":"2023-08-22T23:44:23.332Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":6159,"end":6245},{"type":"TextQuoteSelector","exact":"Most competitive neural sequence transduction models have an encoder-decoder structure","prefix":"15] and [8].3 Model Architecture","suffix":" [5, 2, 29].Here, the encoder ma"}]}]}
>```
>%%
>*%%PREFIX%%15] and [8].3 Model Architecture%%HIGHLIGHT%% ==Most competitive neural sequence transduction models have an encoder-decoder structure== %%POSTFIX%%[5, 2, 29].Here, the encoder ma*
>%%LINK%%[[#^iewr1lf5x5f|show annotation]]
>%%COMMENT%%
>most models like this use an encoder-decoder structure
>%%TAGS%%
>
^iewr1lf5x5f


>%%
>```annotation-json
>{"created":"2023-08-22T23:45:07.857Z","text":"**encoder** maps input sequence to sequence of continuous representations:\n\n$f: (x_1, \\dots, x_n) \\rightarrow (z_1, \\dots, z_n)$","updated":"2023-08-22T23:45:07.857Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":6267,"end":6274},{"type":"TextQuoteSelector","exact":"encoder","prefix":" structure [5, 2, 29].Here, the ","suffix":" maps an input sequence of symbo"}]}]}
>```
>%%
>*%%PREFIX%%structure [5, 2, 29].Here, the%%HIGHLIGHT%% ==encoder== %%POSTFIX%%maps an input sequence of symbo*
>%%LINK%%[[#^ezq2tw5r5m8|show annotation]]
>%%COMMENT%%
>**encoder** maps input sequence to sequence of continuous representations:
>
>$f: (x_1, \dots, x_n) \rightarrow (z_1, \dots, z_n)$
>%%TAGS%%
>
^ezq2tw5r5m8


>%%
>```annotation-json
>{"created":"2023-08-22T23:47:37.687Z","text":"given $\\mathbf{z}$ **decoder** generates an output sequence $\\mathbf{y}$ of symbols one element at a time:\n\n$f^{-1}: (z_1, \\dots, z_n) \\rightarrow ( y_1, \\dots, y_n )$","updated":"2023-08-22T23:47:37.687Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":6409,"end":6416},{"type":"TextQuoteSelector","exact":"decoder","prefix":"s z = (z1,...,zn). Given z, the ","suffix":" then generates an outputsequenc"}]}]}
>```
>%%
>*%%PREFIX%%s z = (z1,...,zn). Given z, the%%HIGHLIGHT%% ==decoder== %%POSTFIX%%then generates an outputsequenc*
>%%LINK%%[[#^ui60eka1c6p|show annotation]]
>%%COMMENT%%
>given $\mathbf{z}$ **decoder** generates an output sequence $\mathbf{y}$ of symbols one element at a time:
>
>$f^{-1}: (z_1, \dots, z_n) \rightarrow ( y_1, \dots, y_n )$
>%%TAGS%%
>
^ui60eka1c6p


>%%
>```annotation-json
>{"created":"2023-08-22T23:49:52.374Z","text":"model relies on previously generated symbols","updated":"2023-08-22T23:49:52.374Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":6496,"end":6537},{"type":"TextQuoteSelector","exact":"At each step the model is auto-regressive","prefix":" symbols one element at a time. ","suffix":"[9], consuming the previously ge"}]}]}
>```
>%%
>*%%PREFIX%%symbols one element at a time.%%HIGHLIGHT%% ==At each step the model is auto-regressive== %%POSTFIX%%[9], consuming the previously ge*
>%%LINK%%[[#^wz42qcdjx2|show annotation]]
>%%COMMENT%%
>model relies on previously generated symbols
>%%TAGS%%
>
^wz42qcdjx2


>%%
>```annotation-json
>{"created":"2023-08-22T23:51:44.861Z","text":"each encoder layer has two sub layers ","updated":"2023-08-22T23:51:44.861Z","document":{"title":"Attention is All you Need","link":[{"href":"urn:x-pdf:36c935f5b33714825d5ae1af9c0507b5"},{"href":"vault:/pdf/attention-is-all-you-need-2017.pdf"}],"documentFingerprint":"36c935f5b33714825d5ae1af9c0507b5"},"uri":"vault:/pdf/attention-is-all-you-need-2017.pdf","target":[{"source":"vault:/pdf/attention-is-all-you-need-2017.pdf","selector":[{"type":"TextPositionSelector","start":6871,"end":6971},{"type":"TextQuoteSelector","exact":"Encoder: The encoder is composed of a stack of N = 6 identical layers. Each layer has twosub-layers.","prefix":"y.3.1 Encoder and Decoder Stacks","suffix":" The first is a multi-head self-"}]}]}
>```
>%%
>*%%PREFIX%%y.3.1 Encoder and Decoder Stacks%%HIGHLIGHT%% ==Encoder: The encoder is composed of a stack of N = 6 identical layers. Each layer has twosub-layers.== %%POSTFIX%%The first is a multi-head self-*
>%%LINK%%[[#^j0k53rt1yh|show annotation]]
>%%COMMENT%%
>each encoder layer has two sub layers 
>%%TAGS%%
>
^j0k53rt1yh

[^1]: ByteNet, ConvS2S