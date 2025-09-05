# SOLUTION.md — Lab 2: UrlCount (Hadoop Streaming, Python)

## Brief Description
I implemented UrlCount using Hadoop **Streaming** with Python:
- **Mapper (UrlMapper.py):** extracts `href="..."` / `href='...'` with regex and emits `<url>\t1`.
- **Reducer (UrlReducer.py):** sums counts per URL and prints only those with **total > 5** as `<url> <count>`.

## Software Needed
- GCP **Dataproc** (Hadoop/YARN installed by default)
- **Python 3.x**
- **HDFS**

## Output URls (Count > 5):
#cite_note-releases-2 7
/wiki/Doi_(identifier) 17
/wiki/ISBN_(identifier) 18
/wiki/MapReduce 6
mw-data:TemplateStyles:r999302996 110

## Why a Java Combiner Can Change Results Here  
A combiner runs before the final reducer and can perform local aggregation. If filtering (count > 5) happens in a combiner or mapper, keys that exceed 5 only after global aggregation (for example, 3 + 3 from two mappers) might be incorrectly dropped. Therefore, the > 5 filter must be applied only in the final reduce stage.  

## Dataproc Timing Comparison  
Cluster A (1 master + 2 workers): real = 1m5.980s  

Cluster B (1 master + 4 workers): real = 1m8.139s  

## Discussion: 
With this small dataset, startup and shuffle overhead are the main factors. Adding workers did not speed up the job; the 2-worker cluster was slightly faster because of lower coordination and shuffle overhead, which was somewhat surprising.  

## Collaboration  
I got help from AI whenever I was stuck.