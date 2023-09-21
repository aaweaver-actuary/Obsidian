[[BERT is short for Bidirectional Encoder Representations from Transformers|BERT]] #transformer [[Python]] 

[Hugging Face documentation](https://huggingface.co/bert-base-cased)

You can use this model directly with a pipeline for masked language modeling:

```python
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-cased')
unmasker("Hello I'm a [MASK] model.")

[{'sequence': "[CLS] Hello I'm a fashion model. [SEP]",
  'score': 0.09019174426794052,
  'token': 4633,
  'token_str': 'fashion'},
 {'sequence': "[CLS] Hello I'm a new model. [SEP]",
  'score': 0.06349995732307434,
  'token': 1207,
  'token_str': 'new'},
 {'sequence': "[CLS] Hello I'm a male model. [SEP]",
  'score': 0.06228214129805565,
  'token': 2581,
  'token_str': 'male'},
 {'sequence': "[CLS] Hello I'm a professional model. [SEP]",
  'score': 0.0441727414727211,
  'token': 1848,
  'token_str': 'professional'},
 {'sequence': "[CLS] Hello I'm a super model. [SEP]",
  'score': 0.03326151892542839,
  'token': 7688,
  'token_str': 'super'}]
```



Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = BertModel.from_pretrained("bert-base-cased")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

This is how to #fine-tune #bert-base-cased on [[Amazon]] [[Amazon Sagemaker|Sagemaker]]:

```python
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFace

try:
	role = sagemaker.get_execution_role()
except ValueError:
	iam = boto3.client('iam')
	role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']
		
hyperparameters = {
	'model_name_or_path':'bert-base-cased',
	'output_dir':'/opt/ml/model'
	# add your remaining hyperparameters
	# more info here https://github.com/huggingface/transformers/tree/v4.26.0/examples/pytorch/text-classification
}

# git configuration to download our fine-tuning script
git_config = {'repo': 'https://github.com/huggingface/transformers.git','branch': 'v4.26.0'}

# creates Hugging Face estimator
huggingface_estimator = HuggingFace(
	entry_point='run_glue.py',
	source_dir='./examples/pytorch/text-classification',
	instance_type='ml.p3.2xlarge',
	instance_count=1,
	role=role,
	git_config=git_config,
	transformers_version='4.26.0',
	pytorch_version='1.13.1',
	py_version='py39',
	hyperparameters = hyperparameters
)

# starting the train job
huggingface_estimator.fit()```

[[Hugging Face script to fine-tune BERT for text classification]]

[[Convert tensorflow to pytorch]]

`
