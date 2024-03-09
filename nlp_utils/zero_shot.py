from transformers import pipeline

def zero_shot(self, *args, **kwargs):
        classifier = pipeline("zero-shot-classification")
        txt = [
            'Poetry is a lot like truth, and people hate poetry',
            'I bought a large car yesterday',
            'We mean to know the world spiritually and philosophically',
            'We strive to achieve results, and that is our goal, our motto'
        ]
        candidate_labels = ["abstract concept", "ideal", "theoretical"]
        res = classifier(txt, candidate_labels)
        for item in res:
            print('>>> ', item['sequence'], f'The label was {item["labels"][0]} with {round(item["scores"][0], 2)} percent confidence\n\n')