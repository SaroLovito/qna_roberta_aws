from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

context = 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
question = 'Why is model conversion important?'

def nlp_qna(context, question):

    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': question ,
        'context': context
    }
    result = nlp(QA_input)


    return result



