from __future__ import print_function
import fitz
import glob
import sys, time, re
import nltk
import numpy


def work_with_txt(txt_path):
    k_tokens=[]
    keylist=[]
    with open(txt_path,"r") as file:
        for line in file:
            line=line.strip('\n')
            k_tokens=nltk.word_tokenize(line)
            keylist.append(k_tokens)
    file.close()
    print(keylist)
    return keylist

def work_with_pdfs(pdfs):

    #! working with pages
    paragraph_info=[]

    for i, pdf in enumerate(pdfs):
        doc=fitz.open(pdf)

       # pdf_name=os.path.basename(pdf)
        for page in doc:
            page2text=page.getText("blocks")
            page_no=page.number
            for item in page2text:
                paragraph_no=item[5]
                paragraph=item[4]
                paragraph_tokens=nltk.word_tokenize(paragraph)
                paragraph_info.append(page_no)
                paragraph_info.append(paragraph_no)
                paragraph_info.append(paragraph_tokens)
        doc.close()
    print(paragraph_info)
    return paragraph_info


def extract(keylist,pdfs_tokens):
    extract=[]
    blocks=pdfs_tokens[2:len(pdfs_tokens):3]
    for k, key in enumerate(keylist):
        kkey=' '.join(key)
        size=len(key)
        # print(kkey,size)
        for i, block in enumerate(blocks):
            for j, token in enumerate(block):
                ttoken=' '.join(block[j:j+size])
                if ttoken==kkey:
                    extract.append(ttoken)
    print(extract)
    return(extract)



if __name__=='__main__':

    txt_path="./data/datasets/keywords"
    pdfs_path=glob.glob("./data/datasets/*.pdf")

    keylist=work_with_txt(txt_path)
    pdfs_list=work_with_pdfs(pdfs_path)

    extract(keylist,pdfs_list)





























