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


Q&A

Q: Why cant we directly use the index of the maximum on the smoothed curve?
A: The position of the maximum value may not be the same as the position of the maximum value on the original curve.

![image](https://user-images.githubusercontent.com/52102632/172809057-d8383807-a512-4b0d-b0e9-6f02a231cf5e.png)


Q: How do I make the detection more sensitive?
A: Reduce the amount of smoothing done.

![image](https://user-images.githubusercontent.com/52102632/172808789-0c58ae92-62ac-4bd4-bde1-df996fd6ee3b.png)



Q:Why cant we just find the top x max values?
A: The top max values may be concentrated on a single peak.

![image](https://user-images.githubusercontent.com/52102632/172808269-a352b735-d19c-4b6f-9245-50dfa6f34a6a.png)




References:
https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way
https://stackoverflow.com/questions/19936033/finding-turning-points-of-an-array-in-python
