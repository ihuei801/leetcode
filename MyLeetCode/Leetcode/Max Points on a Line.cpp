//refer to http://blog.csdn.net/doc_sgl/article/details/17103427
//1. if the slope of ponit_a and point_b is equal to point_a and point_c, then point_a, point_b, point_c are in the same line.

/*
  struct Point {
      int x;
      int y;
      Point() : x(0), y(0) {}
      Point(int a, int b) : x(a), y(b) {}
  };
*/
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        int max_num = 0;
        map<float, int>slope;

        for (int i = 0; i < points.size(); i++)
        {
            int duplicate;
            //the initial value of duplicate is 1 because point[i] itself should be counted.
            duplicate = 1;
            slope.clear();
            //case: points only has one point.
            slope[INT_MIN] = 0;
            for (int j = i+1; j < points.size(); j++)
            {
                if (points[i].x == points[j].x && points[i].y == points[j].y)
                {
                    duplicate++;
                    continue;
                }

                if (points[i].x == points[j].x)
                    slope[INT_MAX]++;
                else
                {
                    //careful about the (float) casting
                    float curr_slope = (float)(points[i].y - points[j].y) / (float)(points[i].x - points[j].x);
                    slope[curr_slope]++;
                }
            }
            map<float, int>::iterator it = slope.begin();
            for (;it != slope.end(); it++)
            {
                //count the duplicate number of points[i]
                max_num = max(max_num, it->second+duplicate);
            }
        }
        return max_num;
    }
};