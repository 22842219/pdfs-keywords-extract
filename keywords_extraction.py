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

    for index,item in enumerate(pdfs_tokens):
        if index%3==0:
            page_no=item+1
            # print(page_no)
        elif index%3==1:
            paragraph_no=item+1
            # print(paragraph_no)
        else:
            blocks=item
            for k, key in enumerate(keylist):
                kkey=' '.join(key)
                size=len(key)
                for i, token in enumerate(blocks):
                    ttoken=' '.join(blocks[i:i+size])
                    if ttoken==kkey:
                        extract.append(ttoken)
                        extract.append(page_no)
                        extract.append(paragraph_no)
                        extract.append(i)


    print(extract)
    return(extract)



if __name__=='__main__':

    txt_path="./data/datasets/keywords"
    pdfs_path=glob.glob("./data/datasets/*.pdf")

    keylist=work_with_txt(txt_path)
    paragraph_info=work_with_pdfs(pdfs_path)

    extract=extract(keylist,paragraph_info)





























