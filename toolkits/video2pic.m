%% 读取视频
 
video_file='output(2).mp4';
 
video=VideoReader(video_file);
 
frame_number=floor(video.Duration * video.FrameRate);
video.FrameRate
frame_number
%% 分离图片
for i=1:frame_number
    if(i<10)
        image_name=strcat('000',num2str(i));
    end
    if(100>i && i>9)
        image_name=strcat('00',num2str(i));
    end
    if(1000>i && i>99)
        image_name=strcat('0',num2str(i));
    end
    if(i>999)
        image_name=strcat(num2str(i));
    end
	image_name=strcat(image_name,'.jpg');
 
	I=read(video,i);	%读出图片
 
	imwrite(I,image_name,'jpg'); 	%写图片
 
	I=[];
 
end