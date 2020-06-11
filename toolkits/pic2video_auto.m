function pic2video_auto(src_dir,picformat)
% 将某个文件夹下某种格式的所有图片合成为视频文件
% picformat : 要读取的图片的格式，如png、jpg等形式，字符串数组
% example : pic2video( './','jpg');
    if ~exist(src_dir, 'dir')
        error('dir not exist!!!!');
    end
   
    files = dir(src_dir);
    size_files = size(files);
    lengthOfFile = size_files(1);
    fileName = zeros(lengthOfFile-3,1);
    fileName = string(fileName);
    for i=3:lengthOfFile;
        fileName1 = strcat(src_dir,files(i,1).name);
        fileName(i-2) = fileName1;
    end
    
    for i=83:lengthOfFile-3;
        
        str = ['第',num2str(i),'个视频']
        
        frameset = fileName(i)
       %-----------------------------
        box_dir = strcat(frameset,'/groundtruth_rect.txt')
        
        fid = fopen(box_dir);
        [box_arr] = textscan(fid,'%n %n %n %n', 'delimiter', ',');
        box_arr = [box_arr{1} box_arr{2} box_arr{3} box_arr{4}];
        fclose(fid);
        
        aviname = strcat(strrep(frameset,'./','OTB_'),'.avi')
        
        src_dir = strcat(frameset,'/img/');
        
        picname=fullfile( src_dir, strcat('*.',picformat));
        picname=dir(picname);
 
        aviobj = VideoWriter(char(aviname));
        open(aviobj);
 
        for j=1:length(picname)
            picdata=imread(char(fullfile(src_dir,(picname(j,1).name))));
            picdata = insertShape(picdata,'Rectangle',box_arr(j,:),'Color','red','LineWidth',3);%插入ground_truth
 
            if ~isempty( aviobj.Height)
                if size(picdata,1) ~= aviobj.Height || size(picdata,2) ~= aviobj.Width
                    close(aviobj);
                    delete( aviname )
                    error('所有图片的尺寸要相同！！');
                end
            end
            writeVideo(aviobj,picdata);
        end
        close(aviobj);
       %-----------------------------
       
    end
end