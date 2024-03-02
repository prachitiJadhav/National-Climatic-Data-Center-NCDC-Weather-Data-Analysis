# National Climatic Data Center (NCDC) Weather Data Analysis Project

This project involves comprehensive data processing and analysis tasks using a variety of Big Data technologies, including Hadoop, PySpark, Pig, and Hive. The aim is to extract meaningful insights from the National Climatic Data Center (NCDC) records through a series of tasks focusing on wind direction, sky ceiling height, visibility distance, and more.

## Objective

To process and analyze NCDC weather data to calculate averages, ranges, and visibility distances, and to understand weather station data patterns. This project is structured into four parts, each requiring specific Big Data tools and methodologies.

## Project Structure

### Part 1: Average Wind Direction Calculation with Hadoop

- **Goal**: Calculate the monthly average wind direction for each year.
- **Method**: Develop Mapper and Reducer applications in Python and execute them using Hadoop Streaming.
- **Commands**:
    ```bash
    chmod +x avg_temp_map.py
    chmod +x avg_temp_reduce.py
    # Testing locally
    echo "0067011990999991950051507004+68750+023550FM-12+038299999V0203301N00671220001CN9999999N9+00001+99999999999" | ./avg_temp_map.py | sort -k1,1 | ./avg_temp_reduce.py
    # Running on Hadoop
    hadoop jar hadoop-streaming-2.7.3.jar -file avg_temp_map.py -mapper avg_temp_map.py -file avg_temp_reduce.py -reducer avg_temp_reduce.py -input /project/ProjectData/* -output /outputproject10
    ```

### Part 2: Sky Ceiling Height Range Calculation with PySpark

- **Goal**: Calculate the range of sky ceiling heights for each weather station ID.
- **Method**: Implement a Python application using PySpark.
- **Commands**:
    ```bash
    spark-submit --master local pySpark_HeightID.py /project/ProjectData/* /project/outputquestion0007/
    ```

### Part 3: Visibility Distance Retrieval with Hadoop

- **Goal**: Extract and record visibility distances along with weather station IDs.
- **Method**: Develop Mapper and Reducer applications for data extraction and summarization.
- **Commands**:
    ```bash
    chmod +x map3.py
    chmod +x visibility_distance_reduce.py
    # Running on Hadoop
    hadoop jar hadoop-streaming-2.7.3.jar -file map3.py -mapper map3.py -file visibility_distance_reduce.py -reducer visibility_distance_reduce.py -input /project/ProjectData/* -output /outputproject03
    ```

### Part 4: Data Analysis with Pig and Hive

- **Goal**: Further analyze the data to find the range of visibility distances and average visibility distance for each weather station ID using Pig and Hive.
- **Pig Commands**:
    ```bash
    pig -x local
    ```
- **Hive Commands**:
    ```sql
    DROP TABLE IF EXISTS records9000;
    CREATE TABLE records9000 (id INT, visibility INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';
    LOAD DATA LOCAL INPATH 'ProjectData/question3output.txt' INTO TABLE records9000;
    SELECT id, AVG(visibility) FROM records9000 WHERE visibility != 99999 GROUP BY id;
    ```

## Data and Resources

The dataset utilized in this project is sourced from the National Climatic Data Center (NCDC) and is provided in files above.

Submissions include developed applications (in Java or Python), text files generated, and a comprehensive list of commands used throughout the project for data processing and analysis tasks.

## Visuals

- (Optional) Include screenshots or visuals of your data analysis process, results, or any interesting findings here. Replace `path/to/image.png` with your image paths.
    ![Data Analysis Visual](path/to/image.png)

## Conclusion

This project showcases the application of Big Data technologies in processing and analyzing climate data, providing valuable insights into weather patterns and phenomena.

