from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.similarities import Similarity
from gensim import corpora, models
import numpy as np
import jieba

def preprocess(sentence):
    # 使用jieba分词进行分词
    words = jieba.cut(sentence)

    # 去掉停用词
    stopwords = ['的', '了', '是', '在', '什么']
    words = [word for word in words if word not in stopwords]

    # 将单词用空格连接起来并返回
    return ' '.join(words)

def similarity(s1, s2):
    '''暴力求解两个句子的相似度

    Args:
        s1: 第一个句子
        s2: 第二个句子

    Returns: 返回两个句子的相似度

    '''

    # 对两个句子进行预处理
    s1_processed = preprocess(s1)
    s2_processed = preprocess(s2)

    # 将两个句子合并成一个文档
    documents = [s1_processed, s2_processed]

    # 计算TF-IDF特征向量
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # 计算余弦相似度
    cosine_sim = cosine_similarity(tfidf_matrix)[0][1]

    return cosine_sim


def calculate_similarity(sentence1, sentence2):
    '''用了Gensim库中的语料库、词典、TF-IDF模型和相似度计算工具。求解两个句子意思上的相似度
    Args:
        sentence1:
        sentence2:

    Returns:返回这两个句子的余弦相似度
    '''

    # 对句子进行分词
    seg_sentence1 = jieba.lcut(sentence1)
    seg_sentence2 = jieba.lcut(sentence2)

    # 构建语料库
    corpus = []
    corpus.append(seg_sentence1)
    corpus.append(seg_sentence2)

    # 构建词典
    dictionary = corpora.Dictionary(corpus)

    # 将语料库转化为向量形式
    corpus_vec = [dictionary.doc2bow(text) for text in corpus]

    # 训练TF-IDF模型
    tfidf_model = models.TfidfModel(corpus_vec)

    # 将两个句子转换为向量形式
    sentence1_vec = tfidf_model[dictionary.doc2bow(seg_sentence1)]
    sentence2_vec = tfidf_model[dictionary.doc2bow(seg_sentence2)]

    # 计算两个句子的相似度
    similarity = Similarity('-Similarity-index', corpus_vec, num_features=len(dictionary))
    cosine_sim = similarity[sentence1_vec][0]

    return cosine_sim

def find_most_similar_sentence_index(sentences, target_sentence):
    '''

    Args:
        sentences: 查找的文本list
        target_sentence: 查找的目标句子

    Returns: 目标句子与列表中的所有句子比较，返回相似度最高的下标

    '''
    # 计算目标句子和列表中每个句子的相似度
    similarities = [similarity(target_sentence, s) for s in sentences]

    # 找到相似度最大的句子的下标
    max_index = np.argmax(similarities)
    return max_index