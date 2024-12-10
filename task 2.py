import pandas as pd
from sklearn.metrics import cohen_kappa_score

# convert excel sheet to DataFrame object
file_path = r'C:\Users\amnes\Downloads\Task 2 (Annotation and Agreement) .xlsx'
data = pd.read_excel(file_path)

def collect_annotation(data):
    annotators = data.columns[1:]
    annotation_data = {}
    for annotator in annotators:
        annotator_annotations = data[annotator].tolist()
        annotation_data[annotator] = annotator_annotations
    return annotation_data

class Annotator:
    def __init__(self, name, annotator_annotations):
        self.name = name
        self.annotator_annotations = annotator_annotations

    def cohens_kappa(self, other_annotator: 'Annotator'):
        if not isinstance(other_annotator, Annotator):
            raise TypeError("The input must be an instance of Annotator.")
        
        if len(self.annotator_annotations) != len(other_annotator.annotator_annotations):
            raise ValueError("Annotation lists must be of the same length to calculate Cohen's kappa.")
        
        return cohen_kappa_score(self.annotator_annotations, other_annotator.annotator_annotations)






"""annotators = data.columns.tolist()
annotations = data.values.tolist()
print(annotators, annotations)
cm = sklearn.metrics.confusion_matrix(readerA, readerB)
print(cm)"""

if __name__ == "__main__":

    annotation_data = collect_annotation(data)
    
    annotators = []
    for name, annotator_annotations in annotation_data.items():
        annotator = Annotator(name=name, annotator_annotations=annotator_annotations)
        annotators.append(annotator)
    print(annotators)
    cohens_kappa_scores = {}
    for annotator in annotators:
        for other_annotator in annotators:
            if annotator == other_annotator:
                continue  # Skip self-comparison
            cohens_kappa = annotator.cohens_kappa(other_annotator)
            cohens_kappa_scores[f"between {annotator.name} and {other_annotator.name}"] = cohens_kappa
    print(cohens_kappa_scores)

        
