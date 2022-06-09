# peakDetection
Detecting Peaks in a dataset

![image](https://user-images.githubusercontent.com/52102632/172800779-59e4ab20-e53c-4d2c-8707-3b18511eec3c.png)

Detection of multiple peaks in a database without cluttering the output.


Method:
1. Smoothing of y value via Moving Average (The smoother the y_smooth, the lesser the detection of peaks. The less smooth the y_smooth, the greater number of peaks detected.

2. Detection of the turning points by finding turning points on y_smooth.

3. Using the Index of the minimum on y_smooth, slice the x value.
![image](https://user-images.githubusercontent.com/52102632/172804778-d8451b2f-829e-4cef-8850-585e7a1c98a7.png)


4. For each slice, find the actual max Y.

Inputs: list/ pd.series of X  
        list/ pd.series of Y
        
Output: list of tuples(X,Y)
        E.G [(1,3),(2,3)]
        
To Find the throughs of a graph, use maximum points and find minimum points within the maximum point slices
