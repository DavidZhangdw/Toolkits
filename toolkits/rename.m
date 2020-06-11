clear
files = dir('*.jpg');
len=length(files);
for i=1:len
    oldname=['"',files(i).name,'"'];
    newname=['frame',num2str(i),'.jpg'];
    command = ['rename' 32 oldname 32 newname];
    status = dos(command);
    if status == 0
        disp([oldname, ' 已被重命名为 ', newname])
    else
        disp([oldname, ' 重命名失败!'])
    end
end