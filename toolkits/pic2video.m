function pic2video(dn, picformat,aviname)
% CreatVideoFromPic(dn, picformat,aviname)
% 将某个文件夹下某种格式的所有图片合成为视频文件
% dn : 存储图片的文件夹
% picformat : 要读取的图片的格式，如png、jpg等形式，字符串数组
% aviname   : 存储的视频的文件名
% example : pic2video( './', 'png','presentation.avi');
 
    if ~exist(dn, 'dir')
        error('dir not exist!!!!');
    end
    picname=fullfile( dn, strcat('*.',picformat));
    picname=dir(picname);
 
    aviobj = VideoWriter(aviname);
 
    open(aviobj);
 
    for i=1:length(picname)
        picdata=imread( fullfile(dn, (picname(i,1).name)));
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
end