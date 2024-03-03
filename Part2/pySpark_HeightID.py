from pyspark import SparkContext
import sys
def main():
	#create a sparkcontext
   sc = SparkContext(appName='HeightbyUSAFID')

	#Import the input file
   #input rdd = sc.textFile('path')

   #alternative, provide the i/p path from the command line
   input_file=sys.argv[1]
   input_rdd=sc.textFile(input_file)

   #filter out records with invalid quality values and missing sky ceiling height
   filtered_rdd = input_rdd.filter(lambda line: line[70:75] != "99999" and int(line[75:76]) in [0,1,4,5,9])

   #extract the ID and sky ceiling height and convert them into pairs
   id_height_rdd=filtered_rdd.map(lambda line: (line[4:10],int(line[70:75])))

   #calculate the range height for each ID
   max_id_rdd=id_height_rdd.reduceByKey(lambda id1, id2:max(id1,id2)-min(id1,id2))
   
  
   #save the output to a final output file
   
    #alternatively we can provide the external output file
   outputfile=sys.argv[2]
   max_id_rdd.saveAsTextFile(outputfile)
   sc.stop()

if __name__ == '__main__':
   main()