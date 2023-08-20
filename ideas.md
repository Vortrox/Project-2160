- ABS TableBuilder has a bunch of data we can use
- Idea: Analyze the possible data formats we can get from there
- Then order data tables in a consistent format
- Idea: Rank 2 tensor (matrix)- Rows: Features, Columns: Timesteps
- Timestep size: Yearly, because that's the timestep available to us for vehicle data
- Missing year timesteps action? TODO
- Converting monthly timesteps into yearly timesteps? Action: Use average

