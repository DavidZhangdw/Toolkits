
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

our = [
    struct('tracker','HROM-18','auc',0.404,'speed',1.604),...  % log(40)
    struct('tracker','HROM-32','auc',0.435,'speed',1.505),...  % log(32)
    struct('tracker','HROM-48','auc',0.452,'speed',1.388),...  % log(24)
    ];

for i = 1:numel(our)
    plot(our(i).speed,our(i).auc,'MarkerFaceColor',[0 0 255]/255,...
        'MarkerEdgeColor',[0 0 0],'MarkerSize',10,'Marker','^',...
        'LineWidth',1,'Color',[193 221 198]/255); hold on;
    text(our(i).speed+0.06,our(i).auc,our(i).tracker, 'FontName','Times New Roman');
end

results = [
    struct('tracker','DiMP','auc',0.44,'speed',1.6),...  % log(40)
    struct('tracker','LADCF','auc',0.389,'speed',0),...  % log(0.22)
    struct('tracker','MFT','auc',0.385,'speed',0),...  % log(0.45)
    struct('tracker','DaSiamRPN','auc',0.383,'speed',2.079),...  % log(120)
    struct('tracker','UPDT','auc',0.378,'speed',0),...  % log(0.15)
    struct('tracker','DRT','auc',0.356,'speed',0),...  % log(0.15)
    struct('tracker','DeepSTRCF','auc',0.345,'speed',0.477),...  % log(3)
    struct('tracker','SA-Siam-R','auc',0.337,'speed',1.505),...  % log(32)
    struct('tracker','DLSTpp','auc',0.325,'speed',0.869),...  % log(7.4)
    struct('tracker','SRCT','auc',0.31,'speed',0.0569),...  % log(1.12)
    struct('tracker','LSART','auc',0.323,'speed',0.08),...  % log(1)
    struct('tracker','SiamVGG','auc',0.286,'speed',1.5185),...  % log(33)
    struct('tracker','SA-Siam-P','auc',0.286,'speed',1.6989),...  % log(50)
    struct('tracker','CFCF','auc',0.282,'speed',0.3),...  % log(2)
    struct('tracker','ECO','auc',0.28,'speed',0.903),...  % log(8)
    struct('tracker','MCCT','auc',0.274,'speed',0.176),...  % log(1.5)
    struct('tracker','CSRDCF','auc',0.256,'speed',1.1139),...  % log(13)
    struct('tracker','DSiam','auc',1.397,'speed',0.38),...  % log(25)
    struct('tracker','SiamFC','auc',0.188,'speed',1.934),...  % log(86)
    struct('tracker','SiamRPN++','auc',0.414,'speed',1.544),...  % log(35)
    struct('tracker','SiamFC++','auc',0.426,'speed',1.954),...  % log(90)
    struct('tracker','SiamMask','auc',0.38,'speed',1.74),...  % log(55)
    struct('tracker','SPM','auc',0.338,'speed',2.079),...  % log(120)
    struct('tracker','ATOM','auc',0.401,'speed',1.477),...  % log(30)
    ];

line([1.4,1.4],[0.24,0.465],'LineWidth',1,'Color',[0.7 0.7 0.7],'linestyle','--'); hold on;
line([-0.1,2.58],[0.4,0.4],'LineWidth',1,'Color',[0.7 0.7 0.7],'linestyle','--'); hold on;

for i = 1:numel(results)
    plot(results(i).speed,results(i).auc,'MarkerFaceColor',[178 48 158]/255,...
        'MarkerEdgeColor',[0 0 0],'MarkerSize',10,'Marker','o',...
        'LineWidth',1,'Color',[193 221 198]/255); hold on;
    text(results(i).speed+0.06,results(i).auc,results(i).tracker, 'FontName','Times New Roman');
end

grid on
ylim([0.24,0.462]);
set(gca,'linewidth',1,'GridLineStyle',':')
% set(gca,'linewidth',1,'GridLineStyle',':','XTick',[50 75 100 125 150 175 200])
xlim([-0.1,2.58]);
xlabel('Tracking Speed (10^x FPS)', 'FontName','Times New Roman','FontSize',12);
ylabel('EAO', 'FontName','Times New Roman','FontSize',12.5);
title('\textbf{EAO vs. Speed on VOT-2018}', 'FontName','Times New Roman','FontSize',13.5,'Interpreter','latex')
% legend({ 'SPCNet Feature Channel variants', 'SPCNet Resolution variants', 'other real-time trackers'},...
%     'Location','southwest','Interpreter','latex','FontSize',12)
set(gcf, 'position', [200 200 600 405]);
saveas(gcf,'../img/speed_vs_auc_otb2013','pdf');
saveas(gcf,'../img/speed_vs_auc_otb2013','png');
