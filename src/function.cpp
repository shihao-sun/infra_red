#include <stdio.h>
#include <vector>

#include <opencv4/opencv2/opencv.hpp>
#include <opencv4/opencv2/core/core.hpp>
#include <opencv4/opencv2/core/core_c.h>
#include <opencv4/opencv2/highgui.hpp>
#include <opencv4/opencv2/imgproc/imgproc.hpp>
#include <opencv4/opencv2/imgproc/types_c.h>
#include <iostream>
#include <math.h>


using namespace std;
using namespace cv;

int getskewness(int num[300][192][256],float skewness[192][256])    /*getskewness函数功能：求偏度*/
{
    double sum = 0;//求和
    double sum1 =0;//三次方求和
    double length = 0;//数组长度
    double average = 0;//求平均数
    double var = 0; //求方差
    double standard = 0; //求标准差
    double average1 =0;//求三次方平均数
    
    for(int i = 0;i < 192;i++)
    {
        for(int j = 0;j < 256;j++)  
        {
            for(int n = 0;n < 300;n++)
            {
                sum += num[n][i][j];      //求和
                sum1 += num[n][i][j]*num[n][i][j]*num[n][i][j];   //求三次方和
              //  n += 69;
            }
            length = 300;//数组长度
            average = sum / length;//求平均值
            average1 =sum1 / length ;//求三次方均值

            for(int m = 0;m < 300;m++)
            {
                var += pow(num[m][i][j]-average,2)/length;//求方差
             //   m += 69;
            }
  
            standard = pow(var,0.5);//求标准差   
            skewness[i][j] =(average1 - 3 * average * standard * standard-average*average*average)/(standard*standard*standard);

            skewness[i][j] = abs((skewness[i][j] + 0.5) * (510));
            cout << skewness[i][j] << ",";
        }

       
    }

}


void createAlphaMat(Mat &mat,float skewness[192][256])  //create_picture
{
    for (int i = 0; i < mat.rows; ++i)
    {
        for (int j = 0; j < mat.cols; ++j)
        {
            Vec4b&rgba = mat.at<Vec4b>(i,j);
            rgba[0] =skewness[i][j];
            rgba[1] =skewness[i][j];
            rgba[2] =skewness[i][j];
            rgba[3] =0.5;
        }
    }
}



void produce_picture(float skewness[192][256])    //生成偏度图片.png
{
    Mat picture_mat(192,256,CV_8UC4);

    createAlphaMat(picture_mat,skewness);

    vector<int> compression_params;
    compression_params.push_back(cv::IMWRITE_PNG_COMPRESSION);
    compression_params.push_back(0);
    compression_params.push_back(cv::IMWRITE_PNG_STRATEGY);
    compression_params.push_back(cv::IMWRITE_PNG_STRATEGY_DEFAULT);
    cv::imshow("methodTwo1", picture_mat);
    imwrite("_照片.png",picture_mat,compression_params);

}
