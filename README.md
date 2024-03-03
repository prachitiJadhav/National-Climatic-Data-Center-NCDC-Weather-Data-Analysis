# National Climatic Data Center (NCDC) Weather Data Analysis Project

This project involves comprehensive data processing and analysis tasks using a variety of Big Data technologies, including Hadoop, PySpark, Pig, and Hive. The aim is to extract meaningful insights from the National Climatic Data Center (NCDC) records through a series of tasks focusing on wind direction, sky ceiling height, visibility distance, and more.

## Objective

To process and analyze NCDC weather data to calculate averages, ranges, and visibility distances, and to understand weather station data patterns. This project is structured into four parts, each requiring specific Big Data tools and methodologies.

## Project Structure

### Part 1: Average Wind Direction Calculation with Hadoop

#### Goal
Calculate the monthly average wind direction for each observation month from each year in the NCDC weather dataset. This involves processing records to identify and average wind direction values, excluding missing values (coded as '999') and considering only records with good quality ('[01459]').
- **Method**: Develop Mapper and Reducer applications in Python and execute them using Hadoop Streaming.
#### Development Steps
1. **Create Mapper and Reducer Scripts**: Develop Python scripts to serve as the Mapper (`avg_temp_map.py`) and Reducer (`avg_temp_reduce.py`). These scripts will process the input data to calculate the average wind direction.

2. **Set Execution Permissions**: Before running the scripts, ensure they are executable.
    ```bash
    chmod +x avg_temp_map.py
    chmod +x avg_temp_reduce.py
    ```

3. **Local Testing**: Test the Mapper and Reducer scripts locally to ensure they work as expected. Use a sample input line from the NCDC dataset.
    ```bash
    echo "0067011990999991950051507004+68750+023550FM-12+038299999V0203301N00671220001CN9999999N9+00001+99999999999" | ./avg_temp_map.py | sort -k1,1 | ./avg_temp_reduce.py
    ```
   
   ![Part 1/Images/Picture.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture.png)

5. **Copy Data to HDFS**: Before running the Hadoop job, copy the project data from the local filesystem to HDFS.
    ```bash
    cat sample.txt | /home/student9/avg_temp_map.py
    cat sample.txt | /home/student9/avg_temp_map.py | sort -k1,1 | /home/student9/avg_temp_reduce.py
    
    hdfs dfs -copyFromLocal /home/student9/ProjectData/ /home/9student9/project/

    ```
    ![Part 1/Images/Picture1.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture1.png)
    ![Part 1/Images/Picture2.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture2.png)
   
6. **Execute Hadoop Streaming Job**: Run the Hadoop streaming job with the Mapper and Reducer scripts.
    ```bash
    
    hadoop jar hadoop-streaming-2.7.3.jar
    -file /home/student9/avg_temp_map.py    -mapper /home/student9/avg_temp_map.py
    -file /home/student9/avg_temp_reduce.py   -reducer /home/student9/avg_temp_reduce.py
    -input /home/9student9/project/ProjectData/*
    -output /home/9student9/outputproject10

    ```

    Replace `/path/to/hadoop-streaming-2.7.3.jar` with the actual path to your `hadoop-streaming.jar`.

7. **Verify Output**: After the job completes, check the output files in HDFS.
    ```bash
    hdfs dfs -ls /home/9student9/outputproject10/
    hdfs dfs -cat /home/9student9/outputproject10/part-*
    ```
   ![Part 1/Images/Picture3.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture3.png)
   ![Part 1/Images/Picture4.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture4.png)

9. **Copy Output to Local Filesystem**: Optionally, you can copy the output files from HDFS to your local filesystem for further analysis or backup.
    ```bash
    hdfs dfs -copyToLocal /home/9student9/outputproject10/ /home/student9/ProjectData/
    ```
    ![Part 1/Images/Picture5.png](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%201/Images/Picture5.png)

#### Note
Ensure that the input data and scripts are correctly prepared and located in the specified directories. Adjust paths as necessary to fit your environment and Hadoop setup.


### Part 2: Sky Ceiling Height Range Calculation with PySpark

#### Goal: 
Calculate the range of sky ceiling heights for each weather station ID.
- **Method**: Implement a Python application using PySpark.



#### Development Steps
1. **Develop PySpark Application**: Write a Python script (`pySpark_HeightID.py`) that utilizes PySpark to process the NCDC weather dataset. The script should filter out missing values, compute the minimum and maximum sky ceiling heights for each station ID, and then calculate the range for each.

2. **Running the PySpark Job**: Use the `spark-submit` command to run your PySpark application. Specify the master node (in this case, local), the path to your PySpark script, and the input and output directories.
    ```bash
    spark-submit --master local[2] pySpark_HeightID.py /home/9student9/project/ProjectData/* /home/9student9/project/outputquestion0007/
    ```
    Adjust the `--master` option as needed for your environment (e.g., if running on a cluster, you might use `--master yarn`).

3. **Verify Output**: After the PySpark job completes, check the output in HDFS to ensure it contains the expected range calculations for each weather station ID.
    ```bash
    hdfs dfs -ls /home/9student9/project/outputquestion0007/
    hdfs dfs -cat /home/9student9/project/outputquestion0007/part-00*
    ```
    ![picture1](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part2/Images/Picture1.png)
    ![picture2](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part2/Images/Picture2.png)

4. **Copy Output to Local Filesystem**: If necessary, you can copy the output files from HDFS to your local filesystem for further analysis or for safekeeping.
    ```bash
    hdfs dfs -copyToLocal /home/9student9/project/outputquestion0007/ /home/student9/ProjectData/
    ```
    ![picture3](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part2/Images/Picture3.png)

#### Note
- Ensure that your PySpark script (`pySpark_HeightID.py`) is correctly implemented to filter, map, reduce, and calculate the range of sky ceiling heights as specified.
- Adjust the paths used in the commands to match your project directory structure and Hadoop/Spark environment.
- The `local[2]` option in the `spark-submit` command specifies running in local mode with 2 cores. Adjust this according to the capabilities of your machine or the specifications of your cluster environment.

### Part 3: Visibility Distance Retrieval with Hadoop

#### Goal
The goal is to develop Mapper and Reducer applications that retrieve USAF weather station ID and visibility distance (in meters) from NCDC records. It specifically targets records where '999999' indicates missing values and '[01459]' denote good quality values. The output should be a text file containing the USAF weather station ID and visibility distance data.

#### Development Steps
1. **Prepare Python Mapper and Reducer Scripts**:
   - Develop a Mapper script (`map3.py`) to parse each line of the input data and extract the USAF weather station ID and visibility distance.
   - Develop a Reducer script (`visibility_distance_reduce.py`) to aggregate and process data extracted by the Mapper.

2. **Set Execution Permissions**: Before testing or running your scripts on Hadoop, ensure they have execution permissions.
    ```bash
    chmod +x map3.py
    chmod +x visibility_distance_reduce.py
    ```

3. **Local Testing**:
   - It's a good practice to test your Mapper and Reducer scripts locally before executing them on Hadoop.
    ```bash
    cat sample.txt | /home/student9/map3.py
    cat sample.txt | /home/student9/map3.py | sort -k1,1 | /home/student9/visibility_distance_reduce.py
    ```
    ![Image1](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%203/Images/Picture1.png)
   
    ![Image2](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%203/Images/Picture2.png)

4. **Running on Hadoop**:
   - Use Hadoop streaming to execute your Mapper and Reducer scripts. Make sure to specify the correct paths for your scripts and data.
    ```bash
    hadoop jar hadoop-streaming-2.7.3.jar
    -file /home/student9/map3.py    -mapper /home/student9/map3.py
    -file /home/student9/visibility_distance_reduce.py   -reducer /home/student9/visibility_distance_reduce.py
    -input /home/9student9/project/ProjectData/*
    -output /home/9student9/outputproject03

    ```

5. **Verifying Output**:
   - After the Hadoop job completes, check the output to ensure it's as expected.
    ```bash
    hdfs dfs -ls /home/9student9/outputproject03/
    hdfs dfs -cat /home/9student9/outputproject03/part-*
    ```
    ![Image3](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%203/Images/Picture3.png)
    ![Image4](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%203/Images/Picture4.png)

6. **Copy Output to Local Filesystem**:
   - If needed, copy the output file from HDFS to your local filesystem for further use or analysis.
    ```bash
    hdfs dfs -copyToLocal /home/9student9/outputproject03/part-00000 /home/student9/ProjectData/question3output.txt
    ```
    ![Image5](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%203/Images/Picture5.png)
    

#### Note
- Ensure your Mapper and Reducer scripts are correctly implemented to filter out missing values and accurately process visibility distance data.
- Adjust the paths and filenames in the commands according to your project's directory structure and Hadoop environment setup.
- The commands provided assume a Unix-like environment and may need adjustments for other operating systems.


### Part 4: Data Analysis with Pig and Hive

#### Objective
Perform data analysis tasks on the visibility distance data extracted in Part 3 using both Pig and Hive. Specifically, calculate the range of visibility distances for each USAF weather station ID and compute the average visibility distance for each station ID.

#### Pig Analysis

1. **Start Pig Shell**:
   - Launch the Pig shell to interactively execute Pig scripts.
    ```bash
    pig -x local
    ```

2. **Load Data and Define Schema**:
   - Load the text file containing visibility distance data into a Pig relation (`records`).
    ```pig
    records = LOAD 'ProjectData/question3output.txt' AS (id:int, visibility:int);
    DUMP records;
    DESCRIBE records;
    ```
    ![Image1](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%204/Pig/Images/Picture1.png)
    ![Image2](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%204/Pig/Images/Picture2.png)

3. **Group and Aggregate Data**:
   - Group the data by weather station ID (`id`) and calculate the range of visibility distances for each group.
    ```pig
    grouped_records = GROUP records BY id;
    DUMP grouped_records;
    Describe grouped_records;
    visibility_range = FOREACH grouped_records GENERATE group, MAX(records.visibility) - MIN(records.visibility);
 
    ```
    ![Image3](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%204/Pig/Images/Picture3.png)
    

4. **Display Results**:
   - Output the computed visibility ranges.
    ```pig
    DUMP visibility_range;
    ILLUSTRATE visibility_range;

    ```
    ![Image4](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%204/Pig/Images/Picture4.png)
    ![Image5](https://github.com/prachitiJadhav/National-Climatic-Data-Center-NCDC-Weather-Data-Analysis/blob/main/Part%204/Pig/Images/Picture5.png)

#### Hive Analysis
Load the text file into Hive and get the average visibility distance for each USAF weather station ID.


1. **Load Data into Hive**:
   - Start by creating a Hive table (`records9000`) to store the visibility distance data.
    ```sql
    DROP TABLE IF EXISTS records9000;
    CREATE TABLE records9000 (id INT, visibility INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';
    ```

2. **Load Data**:
   - Load the text file into the Hive table.
    ```sql
    LOAD DATA LOCAL INPATH 'ProjectData/question3output.txt'
    OVERWRITE INTO TABLE records9000;
    ```

3. **Data Analysis**:
   - Execute a Hive query to calculate the average visibility distance for each weather station ID, excluding missing values ('99999').
    ```sql
    SELECT id, AVG(visibility)
    FROM records9000
    WHERE visibility != 99999 
    GROUP BY id;
    ```

#### Note
- Adjust the paths, filenames, and table names in the Pig and Hive commands according to your project's directory structure and data schema.
- Ensure that your Pig and Hive scripts accurately handle missing values and compute the desired analysis metrics.
- The commands provided assume a Unix-like environment and may need adjustments for other operating systems.


## Data and Resources

The dataset utilized in this project is sourced from the National Climatic Data Center (NCDC) and is provided in files above.

Submissions include developed applications (in Java or Python), text files generated, and a comprehensive list of commands used throughout the project for data processing and analysis tasks.

## Visuals

- (Optional) Include screenshots or visuals of your data analysis process, results, or any interesting findings here. Replace `path/to/image.png` with your image paths.
    ![Data Analysis Visual](path/to/image.png)

## Conclusion

This project showcases the application of Big Data technologies in processing and analyzing climate data, providing valuable insights into weather patterns and phenomena.

