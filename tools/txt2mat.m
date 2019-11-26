
Path = 'D:\yuanma\转换\siam11\';                   % 设置数据存放的文件夹路径
File = dir(fullfile(Path,'*.txt'));  % 显示文件夹下所有符合后缀名为.txt文件的完整信息
FileNames = {File.name}';            % 提取符合后缀名为.txt的所有文件的文件名，转换为n行1列

Length_Names = size(FileNames,1);    % 获取所提取数据文件的个数
for k = 1 : Length_Names
    % 连接路径和文件名得到完整的文件路径
    %matName = FileNames(k)
   
    K_Trace = strcat(Path, FileNames(k));
     caseFileName = K_Trace{1,1};
    [pathstr,name,suffix]=fileparts(caseFileName); % pathstr 结果为 E:\test ;  name 结果为  test;suffix 结果为  .txt
    % 读取数据（因为这里是.txt格式数据，所以直接用load()函数)
    eval(['res=','load(K_Trace{1,1})',';']);
    savePath= strcat('D:\yuanma\转换\mat11\.mat','');
    saveName =  strcat('','res');
    save(savePath,saveName);
    
    myMat = load(savePath);
    myMat.type='rect';
    info = whos(savePath);
   
    
    a=matfile(savePath);b=whos(a);c=b.size;
    
    myMat.len=c(1,1);
    myMat.annoBegin = 1;
    myMat.startFrame = 1;
    results{1} = myMat; 
    
    
    
    save(savePath,'results');
    
    
    % load(K_Trace)
    % 注意1：eval()函数是括号内的内容按照命令行执行，
    %       即eval(['a','=''2','+','3',';'])实质为a = 2 + 3;
    % 注意2：由于K_Trace是元胞数组格式，需要加{1,1}才能得到字符串
end

% txt = load('E:\pycharm\myTest\1.txt')
% save('E:\pycharm\myTest\test-1.mat','txt')