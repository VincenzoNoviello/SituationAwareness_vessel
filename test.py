import csv
import pdb
from Annotation import AnnotationManager, MonthAnnotation
import datetime
import matplotlib.pyplot as plt

start_date_october2015 = 1443657600000
delta_t_day = 86400000

reader = csv.DictReader(open("ais_brest_synopses.csv"))
manager = AnnotationManager()
print("sono qui")
for row in reader:
    manager.insert_annotation(int(row['timestamp']), row['annotation'])

octo_annotations = manager.octo.count_base_annotations()
nov_annotations = manager.nov.count_base_annotations()
dec_annotations = manager.dec.count_base_annotations()
jan_annotations = manager.jan.count_base_annotations()
feb_annotations = manager.feb.count_base_annotations()
mar_annotations = manager.mar.count_base_annotations()

print(sum(manager.octo.month_annotations.values()))
print(sum(octo_annotations.values()))

print(sum(manager.nov.month_annotations.values()))
print(sum(nov_annotations.values()))

print(sum(manager.dec.month_annotations.values()))
print(sum(dec_annotations.values()))

print(sum(manager.jan.month_annotations.values()))
print(sum(jan_annotations.values()))

print(sum(manager.feb.month_annotations.values()))
print(sum(feb_annotations.values()))

print(sum(manager.mar.month_annotations.values()))
print(sum(mar_annotations.values()))

print(manager.sum_months_annotations().values())

plt.figure(1)
plt.bar(manager.sum_annotations.keys(), manager.sum_annotations.values(), width=0.8)
plt.show()
# plt.plot(list(manager.sum_annotations.keys()), list(manager.sum_annotations.values()))
