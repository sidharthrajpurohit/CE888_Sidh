# In[1]: # Installling library transformers here used as sensors with other return sensors dependencies
get_ipython().system(’pip install pytorch-transformers’)
get_ipython().system(’pip install transformers’)
get_ipython().system(’pip install sentencepiece’)
get_ipython().system(’pip install SpaCy’) get_ipython().system(’pip install google_trans_new’)
get_ipython().system(’pip install nltk’) # In[2]: # Downloading nltk packages import nltk
nltk.download(’punkt’)
nltk.download(’averaged_perceptro n_tagger’)
nltk.download(’stopwords’) # In[3]: # Importing libraries to be used throughout the code import pandas as pd from pandas import DataFrame 43 import numpy as np
 

 
import json from nltk.stem import PorterStemmer import re,string import nltk from nltk.tokenize import word_tokenize from nltk.corpus import stopwords from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer # In[4]: # Data Preporcessing functions # function to remove stopwords from the data def remove_stop_words(mydata): stop_words =
stopwords.words(’english’) allwords = word_tokenize(str(mydata)) text = "" for word in allwords: if word not in stop_words and len(word) > 1: text = text + " " + word return text # This function has been employed to convert the data to lower case def convert_lower_case(mydata): return np.char.lower(mydata) # This function will be used to remove punctuation marks from our data def remove_punctuation(mydata): characters = "!\"#$%&()*+-
./:;<=>?@[\]^_‘{|}~\n" for a in range(len(characters)): mydata = np.char.replace(mydata,
characters[a], ’ ’) mydata = np.char.replace(mydata, " ", " ") mydata = np.char.replace(mydata, ’,’, ’’) 44 return mydata # This function will be used to remove
 

 
links from our data def remove_links(data): mydata = [] for a in data:
mydata.append(re.sub(r’https?://[ A-Za-z0-9./-]+’ , ’’, a)) return mydata # This function will be used to stem our data for better keywords selection def stemming(data): stemmer= PorterStemmer() tokens = word_tokenize(str(data)) new_text
= "" for w in tokens: new_text = new_text + " " + stemmer.stem(w) return new_text # This function will be used to convert numbers to text def convert_numbers(data): tokens
= word_tokenize(str(data)) new_text = "" for w in tokens: try: w
= num2words(int(w)) except: a = 0 new_text = new_text + " " + w new_text = np.char.replace(new_text, "-", " ") return new_text # This function performs all preprocessing in one step def preprocess(mydata): mydata = convert_lower_case(mydata) 45 mydata = remove_stop_words(mydata) mydata = convert_numbers(mydata) mydata
= remove_punctuation(mydata) return mydata # In[1]: # The data is stored in an Amazon Redshift database and a connection has been made to acfrom sqlalchemy import
 

 
create_engine
conn=create_engine(’postgresql:// discovery:M31b8754ea982a8e3b3 4d35ef1ba09a32D@10.60.4.41#
In[2]: # The data is loaded in a pandas dataframe for further processing import pandas as pd dataframe = pd.read_sql(’SELECT * FROM rappidpro.bolbehan_data;’, conn) # In[3]: dataframe # In[7]: # Using the google translate APIs fucntion to translate the incoming text from google_trans_new import google_translator translator = google_translator() # In[8]: # The top 1500 values of message are stored in a variable messages = dataframe[’message’].iloc[1:1500] # In[9]: # The message value is stored in a variable sample = messages[1:1500] # In[10]: # Translating the text using google translate API and appending in a list testfile = [] 46 for a in sample: testfile.append(translator.translate (a)) # In[11]: # Removing links from the incoming values testfinal = [] for a in testfile:
testfinal.append(re.sub(r’https?://[
A-Za-z0-9./-]+’ , ’’, a)) # In[12]: #
Removing empty values from the incoming values test = [x for x in testfinal if x != ’’] # In[13]: # Assigning data in a new variable data = test # Building the transformer to classify data as
 

 
small talk import pandas as pd import torch import gc from transformers import T5Tokenizer, T5ForConditionalGeneration,Adafa ctor from IPython.display import HTML, display import time def train_datatotext(main_data): train_df = main_data batch_size = 4 num_of_batches=len(train_df)/batc h_size 47 if torch.cuda.is_available(): dev = torch.device("cuda:0") print("Running on the GPU") else: dev = torch.device("cpu") print("Running on the CPU") # Initializing the tokenizer tokenizer
= T5Tokenizer.from_pretrained(’t5- base’) model = T5ForConditionalGeneration.from_ pretrained(’t5-
base’,return_dict=True) #moving the model to GPU model.to(dev) optimizer = Adafactor(model.parameters(),lr=1 e-3, eps=(1e-30, 1e-3),
clip_threshold=1.0, decay_rate=-0.8, beta1=None, weight_decay=0.0, relative_step=False, scale_parameter=False, warmup_init=False) model.train() loss_per_10_steps=[] num_of_epochs = 10 for epoch in range(1,num_of_epochs+1):
print(’Running epoch:
{}’.format(epoch)) 48 running_loss=0 isprint=0 for i in
 

 
range(int(num_of_batches)): inputbatch=[] labelbatch=[] new_df=train_df[i*batch_size:i*batc h_size+batch_size] for indx,row in new_df.iterrows(): input =
’WebNLG: ’+ str(row[’Value’]) +’’ labels = row[’Tag’]+’’ inputbatch.append(input) labelbatch.append(labels) torch.cuda.empty_cache() inputbatch=tokenizer.batch_encode
_plus(inputbatch,padding=True,ma x_length=900,retulabelbatch=token izer.batch_encode_plus(labelbatch, padding=True,max_length=600,ret uinputbatch=inputbatch.to(dev) labelbatch=labelbatch.to(dev) # clear out the gradients of all Variables optimizer.zero_grad() # Forward propogation outputs = model(input_ids=inputbatch, labels=labelbatch) loss = outputs.loss loss_num=loss.item() logits = outputs.logits running_loss+=loss_num #for just printing temp_6=int(num_of_batches/6) 49 isprint+=1 # calculating the gradients loss.backward() #updating the params optimizer.step() torch.cuda.empty_cache() gc.collect() running_loss=running_loss/int(nu m_of_batches) print(’Epoch: {} , Running loss:
 

 
{}’.format(epoch,running_loss)) model.save_pretrained(’trip_gen_au g_trend+income_10_b32’)
f=pd.read_csv(’dataset
(1).csv’,encoding=’utf-8’) main_data
= f main_data=main_data.sample(frac= 1).reset_index(drop=True) print(main_data) train_datatotext(main_data) # In[14]: # The model for transformer has been stored in the Active Directory and can be directlyfrom transformers import T5Tokenizer, T5ForConditionalGeneration,Adafa ctor model
=T5ForConditionalGeneration.from
_pretrained(’trip_gen_aug_trend+in come_10_b32’, re# In[15]: # The generate function to fit the incoming data on transformer model def generate(text,model,tokenizer): model.eval() input_ids = tokenizer.encode("WebNLG:{} ".format(text), 50 return_tensors="pt") outputs = model.generate(input_ids, do_sample=False, max_length=60, min_length=2, top_k=120, top_p=0.98, early_stopping=True, num_return_sequences=1) s=[] for o in outputs: s.append(tokenizer.decode(o)) return s # In[16]: # Initialising an
 

 
instance of the same tokenizer tokenizer =
T5Tokenizer.from_pretrained(’t5- base’) orig_data = data # In[17]: # Classifying the text coming in using the model above and appending in a list datageneral = [] for row in orig_data: res3=generate(row,model,tokenize r) datageneral.append((res3[0].replac e(’’,’’).replace(’’,’’).strip())) # In[18]: # Storing the classified data in a dataframe datag = pd.DataFrame(datageneral,columns
= [’tag’]) datag 51 # In[19]: # Storing the loaded data in a df for further processing dataf = pd.DataFrame(data) dataf # In[20]: # concatenating the dfs datas = pd.concat([datag,dataf],axis = 1).dropna() # In[21]: # The concatnenated Dataframe datas # In[22]: # Dropping all tags that are not General datas.drop(datas.loc[datas[’tag’] != ’General’].index, inplace=True) datas # In[23]: # retrieving the text from text keyword pairs datakeyword = datas.iloc[:, 1] # In[24]: # If data tag is General it will be passed through the next steps test = [] # The text will now be preprocessed for d in datakeyword: test.append(str(preprocess(d)))
 

 
test 52 # In[25]: tags = [] import nltk from nltk import word_tokenize,pos_tag for t in test: # Text will be tokenized in this step text = word_tokenize(t) # Tokenized text will be passed through pos tagging function tags.append(nltk.pos_tag(text)) tags[1] # In[26]: # Some of the word tokens will be removed on the basis of their pos tags dt_tags = [] i = 0 for t in tags: dt_tags.append([]) for dt in t: if dt[1] != "DT" and dt[1] != "IN" and
dt[1] != "CC" and dt[1] != "CD" and dt[1] !=dt_tags[i].append(dt) i = i+1 dt_tags # In[27]: # Text tokens will be appended in a list without their tags listoftext = [] j = 0 for t in tags: 53 listoftext.append([]) for v in t: listoftext[j].append(v[0]) j = j+1 listoftext[2] # In[28]: finallist = [] for t in tags: for v in t: finallist.append(v[0]) # In[29]: # to be used in Tf Idf model finallist # In[30]: # initialising the TfIdf vector tiv = TfidfVectorizer() # In[31]:
word_vector=tiv.fit_transform(final list) # In[32]: # In this step we will be applying the transforming the data with TfIdf transformer # This results in a matrix that will shape our search and optimise the results tfidf_transformer=TfidfTransforme r(smooth_idf=True,use_idf=True)
 

 
tfidf_matrix=tfidf_transformer.fit_tr ansform(word_vector) 54 # In[33]: # In this step we will be obtaining the features from our transformation features = tiv.get_feature_names() # In[34]: # We will now be obtaining keywords by sorting the words using TfIdf score # We are obtaining top 50 keywords for each document in the collection for i in range(dataf.shape[0]): dvector=tfidf_matrix[i] df_doc = pd.DataFrame(dvector.T.todense(), index=features, columns=["tfidf"]) df_doc=df_doc.sort_values(by=["tfid f"],ascending=False) keywords=df_doc.index[:500].tolist ()
#data.loc[i,"keywords"]=",".join(ke ywords) # In[35]: words = [’Vagina’,’Intercourse’,’Relationship’
,’Sex’,’Breasts’,’Menstruation’,’cond oms’,keywords = keywords + words # Adding some general keywords to the list of keywords # In[36]: # writing the keywords obtained to a Df keyword = pd.DataFrame(keywords) # In[37]: # Converting the df to a csv
keyword.to_csv(’keywords.csv’, index=False) # In[38]: # Text tokens will be searched through the keywords list and returned if even one match# otherwise the complete list is returned 55 returntxt = [] i =
 

 
0 for v in listoftext: returntxt.append([]) for t in v: if t in keywords: returntxt[i].append(t) elif t not in keywords: returntxt[i].append(t) i = i + 1 returntxt # In[39]: len(datakeyword) ds = datakeyword.values.tolist() len(ds) # In[40]: # Appending the text and df as columns to be viewed together df = [] for t,v in zip(ds,returntxt): df.append([t,v]) The transformer model used to train on the 500 words corpus for hinglish to english code : from fairseq.models import register_model, register_model_architecture from fairseq.models.transformer import ( base_architecture as transformer_base_architecture, 56 ) from fairseq.models.transformer_from_p retrained_xlm import ( TransformerFromPretrainedXLMM odel, ) from pytorch_translate.data.masked_lm_ dictionary import MaskedLMDictionary @register_model("pytorch_translat e_transformer_from_pretrained_xl m") class PytorchTranslateTransformerFrom PretrainedXLMModel( TransformerFromPretrainedXLMM odel ): @classmethod def build_model(cls, args, task): return
 

 
super().build_model(args, task, cls_dictionary=MaskedLMDictionar
y) @register_model_architecture( "pytorch_translate_transformer_fro m_pretrained_xlm", "pytorch_translate_transformer_fro m_pretrained_xlm", ) def base_architecture(args): transformer_base_architecture(args
) The bash script to run the above transformer file: NCCL_ROOT_DIR="$(pwd)/nccl_2.1
.15-1+cuda8.0_x86_64" export NCCL_ROOT_DIR LD_LIBRARY_PATH="${NCCL_ROO T_DIR}/lib:${LD_LIBRARY_PATH}"
export LD_LIBRARY_PATH wget https://download.pytorch.org/mod els/translate/iwslt14/data.tar.gz 57 tar -xvzf data.tar.gz rm -rf checkpoints data.tar.gz && mkdir -p checkpoints CUDA_VISIBLE_DEVICES=0
python3 pytorch_translate/train.py
\ "" \ --arch rnn \ --log-verbose \ -- lr-scheduler fixed \ --force-anneal 200 \ --cell-type lstm \ --sequence- lstm \ --reverse-source \ --encoder- bidirectional \ --max-epoch 100 \ -- stop-time-hr 72 \ --stop-no-best- bleu-eval 5 \ --optimizer sgd \ --lr
0.5 \ --lr-shrink 0.95 \ --clip-norm
5.0 \ --encoder-dropout-in 0.1 \ -- encoder-dropout-out 0.1 \ -- decoder-dropout-in 0.2 \ -- decoder-dropout-out 0.2 \ --
 

 
criterion label_smoothed_cross_entropy \ -- label-smoothing 0.1 \ --batch-size 256 \ --length-penalty 0 \ --unk-
reward -0.5 \ --word-reward 0.25 \
--max-tokens 9999999 \ 58 -- encoder-layers 2 \ --encoder- embed-dim 256 \ --encoder- hidden-dim 512 \ --decoder-layers 2 \ --decoder-embed-dim 256 \ -- decoder-hidden-dim 512 \ -- decoder-out-embed-dim 256 \ -- save-dir checkpoints \ --attention- type dot \ --sentence-avg \ -- momentum 0 \ --num-avg- checkpoints 10 \ --beam 6 \ --no- beamable-mm \ --source-lang de \ -
-target-lang en \ --train-source- text-file data/train.tok.bpe.de \ -- train-target-text-file data/train.tok.bpe.en \ --eval- source-text-file data/valid.tok.bpe.de \ --eval- target-text-file data/valid.tok.bpe.en \ --source- max-vocab-size 14000 \ --target- max-vocab-size 14000 \ --log- interval 10 \ --seed "${RANDOM}" \ 2>&1 | tee -a checkpoints/log
