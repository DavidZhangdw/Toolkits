
% x = [70,104,140,165,183];%64 32 16 8 4
% y = [0.654,0.665,0.658,0.652,0.627];%64 32 16 8 4
% plot(x,y,'MarkerFaceColor',[0 128 224]/255,...
%     'MarkerEdgeColor',[0 0 0],...
%     'MarkerSize',10,...
%     'Marker','o',...
%     'LineWidth',2,...
%     'Color',[186 212 244]/255); hold on
% 
% c = [64 32 16 8 4];
% offset1 = [3 0 0 2 -19];
% offset2 = [-0.005 0 0.025 0.012 -0.018];
% for i = 1:numel(c)
%     if i == 2 continue;end
%     text(x(i)+offset1(i),y(i)+offset2(i),['SPCNet-C-' num2str(c(i)) '-S-125'], 'FontName','Times New Roman');
% end

x = 1.45;
y = 0.708;
plot(x,y,'MarkerFaceColor',[255,224,48]/255,...
    'MarkerEdgeColor',[0 0 0],...
    'MarkerSize',14,...
    'Marker','p',...   % o,+,.,x,s,d,h,p,*
    'LineWidth',1.5,...
    'Color',[191,128,64]/255)  
hold on;
text(x+0.08,y,['\textbf{CSART}'],'FontName','Times New Roman','Interpreter','latex');

results = [
    %struct('tracker','KCF','auc',0.477,'speed',165),...
    %struct('tracker','StructSiam','auc',0.621,'speed',1.653),...  % log(45)
    %struct('tracker','LMCF','auc',0.580,'speed',1.9294),...  % log(85)
    %struct('tracker','CCOT','auc',0.67,'speed',-0.498),...  % log(0.3)
    %struct('tracker','DAT','auc',0.668,'speed',0),...  % log(1)
    %struct('tracker','Staple','auc',0.578,'speed',1.903),...  % log(80)
    %struct('tracker','ACT','auc',0.625,'speed',1.477),...  % log(30)
    %struct('tracker','ECO-HC','auc',0.643,'speed',1.6),...  % log(60)
    %struct('tracker','TADT','auc',0.66,'speed',1.527),...  % log(33.7)
    %struct('tracker','VITAL','auc',0.682,'speed',0.176),...  % log(1.5)
    %struct('tracker','RASNet','auc',0.642,'speed',1.919),...  % log(83)
    %struct('tracker','ASRCF','auc',0.692,'speed',1.447),...  % log(28)
    struct('tracker','CFNet','auc',0.589,'speed',1.87),...  % log(75)
    struct('tracker','ECO','auc',0.691,'speed',0.903),...  % log(8)
    struct('tracker','UPDT','auc',0.702,'speed',0.02),...  % log(8)
    struct('tracker','MCPF','auc',0.628,'speed',0.255),...  % log(1.8)
    struct('tracker','MCCT-H','auc',0.642,'speed',1),...  % log(10)
    struct('tracker','DSLT','auc',0.66,'speed',0.756),...  % log(5.7)
    struct('tracker','BACF','auc',0.621,'speed',1.544),...  % log(35)
    struct('tracker','LSART','auc',0.672,'speed',0),...  % log(1)
    struct('tracker','MDNet','auc',0.678,'speed',0.04),...  % log(1.1)
    struct('tracker','TCNN','auc',0.654,'speed',0),...  % log(1)
    struct('tracker','SiamFC','auc',0.582,'speed',1.934),...  % log(86)
    struct('tracker','ADNet','auc',0.646,'speed',0.477),...  % log(3)
    struct('tracker','EAST','auc',0.629,'speed',2.2),...  % log(159)
    struct('tracker','CREST','auc',0.623,'speed',0.38),...  % log(2.4)
    struct('tracker','SRDCF','auc',0.623,'speed',0.778),...  % log(6)
    struct('tracker','TRACA','auc',0.603,'speed',2),...  % log(101)
    struct('tracker','SA-Siam','auc',0.657,'speed',1.699),...  % log(50)
    struct('tracker','SiamRPN','auc',0.637,'speed',2.3),...  % log(200)
    struct('tracker','DSiamM','auc',0.605,'speed',1.255),...  % log(18)
    struct('tracker','DaSiamRPN','auc',0.658,'speed',2.2),...  % log(160)
    struct('tracker','ATOM','auc',0.671,'speed',1.477),...  % log(30)
    struct('tracker','DiMP50','auc',0.684,'speed',1.6),...  % log(40)
    struct('tracker','GradNet','auc',0.639,'speed',1.903),...  % log(80)
    struct('tracker','SPM','auc',0.687,'speed',2.07),...  % log(120)
    struct('tracker','SiamRPNpp','auc',0.696,'speed',1.54),...  % log(35)
    struct('tracker','PTAV','auc',0.635,'speed',1.398),...  % log(25)
    ];

line([1.4,1.4],[0.55,0.715],'LineWidth',1,'Color',[0.7 0.7 0.7],'linestyle','--'); hold on;

for i = 1:numel(results)
    plot(results(i).speed,results(i).auc,'MarkerFaceColor',[193 221 198]/255,...
        'MarkerEdgeColor',[0 0 0],'MarkerSize',10,'Marker','o',...
        'LineWidth',1,'Color',[193 221 198]/255); hold on;
    text(results(i).speed+0.06,results(i).auc,results(i).tracker, 'FontName','Times New Roman');
end

grid on
ylim([0.57,0.715]);
set(gca,'linewidth',1,'GridLineStyle',':')
% set(gca,'linewidth',1,'GridLineStyle',':','XTick',[50 75 100 125 150 175 200])
xlim([-0.1,2.58]);
xlabel('Tracking Speed (10^x FPS)', 'FontName','Times New Roman','FontSize',12);
ylabel('Success rate (AUC)', 'FontName','Times New Roman','FontSize',12.5);
title('\textbf{Success rate (OPE) v.s. Speed on OTB-2015}', 'FontName','Times New Roman','FontSize',13.5,'Interpreter','latex')
% legend({ 'SPCNet Feature Channel variants', 'SPCNet Resolution variants', 'other real-time trackers'},...
%     'Location','southwest','Interpreter','latex','FontSize',12)
set(gcf, 'position', [200 200 600 405]);
saveas(gcf,'../img/speed_vs_auc_otb2013','pdf');
saveas(gcf,'../img/speed_vs_auc_otb2013','png');
