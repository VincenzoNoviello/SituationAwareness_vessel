import pdb
import datetime
class MonthAnnotation:
    def __init__(self):
        self.month_annotations = {}
        self.annotation_simple_dict = {
            "10000000": 0,
            "01000000": 0,
            "00100000": 0,
            "00010000": 0,
            "00001000": 0,
            "00000100": 0,
            "00000010": 0,
            "00000001": 0
        }

    def get_month_annotations(self):
        return self.month_annotations

    def insert(self, annotation):
        # pdb.set_trace()
        if annotation in self.month_annotations:
            self.month_annotations[annotation] += 1
        else:
            self.month_annotations[annotation] = 1
    
    def count_base_annotations(self):
        a = list(self.month_annotations.values())
        j = 0
        for key in self.month_annotations.keys():
            i = 0
            # pdb.set_trace()
            for element in key:
                if element == '1':
                    my_list = list(self.annotation_simple_dict.keys())
                    self.annotation_simple_dict[my_list[i]] += a[j]

                i += 1
            j += 1
        return self.annotation_simple_dict

            

class AnnotationManager:
    def __init__(self):
        self.octo = MonthAnnotation()
        self.nov = MonthAnnotation()
        self.dec = MonthAnnotation()
        self.jan = MonthAnnotation()
        self.feb = MonthAnnotation()
        self.mar = MonthAnnotation()

        self.list_months = [
            self.jan, 
            self.feb, 
            self.mar,
            None, 
            None,
            None,
            None,
            None,
            None,
            self.octo,
            self.nov,
            self.dec
        ]

        self.switcher={
            1: self.jan, 
            2: self.feb, 
            3: self.mar, 
            4: "not",
            5: "not",
            6: "not",
            7: "not",
            8: "not",
            9: "not",
            10: self.octo,
            11: self.nov,
            12: self.dec
        }

        self.sum_annotations = {}
    
    def get_month(self, timestamp):
        date = datetime.datetime.fromtimestamp(timestamp/1000.0)
        return self.switcher.get(date.month)


    def insert_annotation(self, timestamp, annotation):
        month_dict = self.get_month(timestamp)
        month_dict.insert(annotation)

    def sum_months_annotations(self):
        for month in self.list_months:
            if month != None: 
                for key in month.month_annotations:
                    if key in self.sum_annotations:
                        self.sum_annotations[key] += month.month_annotations[key]
                    else:
                        self.sum_annotations[key] = month.month_annotations[key]
        return self.sum_annotations

        
