# 422 Group

## meeting time    
Saturday noon (Oct 3rd)    
Monday 4-6pm     
Friday 4-6pm     
https://developers.google.com/maps/documentation/geocoding/start   
    
http://geoservices.tamu.edu   
   

 Saturday - Oct 3rd
 Group role assignments:   
    * Missy - Repo Master : Clean repo and make sure things are structured nice
    * Lindsay - Build Master / Architect : Overall build plan and design
    * Donna - Documentation Boss / Schedule : Make sure everything is on track and document meetings and project
    * Xuehai - Quality Assurance : Test code and modules to make sure all is running smoothly

 Project Overview / Sketch out MVP:
  we divided the MVP into 3 "chunks" and assigned it to each person:
    1. Parse_gpx (pathname to gpx file) -> pandas dataframe
        * opens gpx file, pulls out lat, long, and time from each trkpt, and stores it in a data structure
        * python xml parser, gpxpy?, Beautiful Soup are all potentially helpful tools
        * Assignment: Donna
        * We'll try to use pandas since it can create an efficient dataframe and we can use pandas function to process the data
        * Donna will be the "pandas shifu" as she has had previous exprecience with pandas
            ** I thought the Kong Fu Panda reference was hilarious! :)
            
    2. Filtered_data (pandas dataframe) -> pandas dataframe with only data points immediately before and after each turn, and with street names added
        * uses a clever algorithm to get rid of unneeded data points (Binary search, Granular Search, etc.)
            ** could be approach 1 or 2 from the assignment document
                *** every data point that has the same street as the one before and after it → you can eliminate it!*
            ** or could be something different, e.g. sample every 30 seconds
        * GOAL -> eliminate unnecessary points + add street names!!
        * Assignment : Xuehai
        
    3. Generate_directions (filtered pandas dataframe) -> csv file
        * generates turn-by-turn directions as a text file
            ** calculates distance between each turn (UTM)
            ** determines if it's a left or right turn (or straight ahead, but the street name changed
            ** writes this information to a csv file
        * Assignment : Missy & Lindsay
        * This will be the most challenging part of the project so we assigned two people to it. 
        
  Rough Timeline: 
    Donna will make a rough schedule by Monday and we'll revise or approve it on Monday.
    
  Other Notes:
    * Donna will also make a fake-sample dataframe and send it to everyone by Monday so everyone can start their work.
    * Until monday: each person will research their work as they're waiting for Donna to send the dataframe. 
    
    
    -------------------------------------------------------------------------------------
Monday - Oct 5th
  Rough Timeline:
      Oct 12th --> Deadline for Donna and Xuehai
      Ocr 21st --> Deadline for Missy and Lindsay
      *Parallel: Xuehai should test the code in parallel as the Quality Assurance person.
  We'll test our individual sections in Jupyter notebook and commit the python executable for that to Github to have in our records.
  Each member went trhough their progress/struggles about their part so far and cleared up any confusion.

    -------------------------------------------------------------------------------------
Wednesday - Oct 7th
   * Met with Professor Young and talked about the overall structure of the project and clearified some details. 
   * At each step, each module will be a python executable (.py) file and there will be a main file that will connect all 3 modules and run the program
   * Module 3 doesn't seem to be as challenging as we thought, so Missy's role is switched to a person that jumps from topics to help members who are struggling.
        * She will currently work on Module 4 with Xuehai.
   * Since we met early this week the normal meeting scheduled on Friday is canceled (unless we need to meet).
   
