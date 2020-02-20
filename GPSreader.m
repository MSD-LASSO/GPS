close all
Data=dlmread('Coordinates2.txt','');

Data=Data(Data(:,1)>0,:);

h1=figure();
plot3(Data(:,1),Data(:,2),Data(:,3),'.')
grid on
xlabel('Latitude (deg)')
ylabel('Longitude (deg)')
zlabel('Altitude (m)')
title('GPS Data')
axis square
means=mean(Data);
medians=median(Data);
stdDev=std(Data);
figure()
subplot(1,3,1)
boxplot(Data(:,1))
ylabel('degrees')
title('Latitude')
subplot(1,3,2)
boxplot(Data(:,2))
title('Longitude')
ylabel('degrees')
subplot(1,3,3)
boxplot(Data(:,3))
title('Altitude')
ylabel('meters')

Tits={['Latitude, StdDev: ' num2str(stdDev(1))],['Longitude, StdDev: ' num2str(stdDev(2))],['Altitude, StdDev: ' num2str(stdDev(3))]};
Labs={'Degrees','Degrees','Meters'};
figure()
for i=1:3
    subplot(1,3,i)
    histogram(Data(:,i),'color','blue','Normalization','probability')
    xlabel(Labs{i})
    ylabel('Relative Frequency')
    title(Tits{i})
end

GraphSaver({'png','fig'},'plots/GPS',0,1)

video=VideoWriter('GPSvid');
open(video)

figure('units','normalized','outerposition',[0 0 1 1])
Az=[45,90,180,0];
El=[45,0,0,90];
xv=[h1.Children().XLim];
yv=[h1.Children().YLim];
zv=[h1.Children().ZLim];
meanToGraph=[xv ones(1,4)*means(1); means(2) means(2) yv means(2) means(2); ones(1,4)*means(3) zv];

for i=1:4
subplot(2,2,i)
% plot3(43.084224,-77.677684,169.164) %from 525 + 30 ft.
plot3(meanToGraph(1,1:2),meanToGraph(2,1:2),meanToGraph(3,1:2),'linewidth',2,'color','red');
hold on
plot3(meanToGraph(1,3:4),meanToGraph(2,3:4),meanToGraph(3,3:4),'linewidth',2,'color','red');
plot3(meanToGraph(1,5:6),meanToGraph(2,5:6),meanToGraph(3,5:6),'linewidth',2,'color','red');
% a(i)=plot3(means(1),means(2),means(3),'s','linewidth',2,'MarkerFaceColor','red','color','red');
xlim(xv)
ylim(yv)
zlim(zv)
view(Az(i),El(i))
grid on
xlabel('Latitude (deg)')
ylabel('Longitude (deg)')
zlabel('Altitude (m)')
axis square

end

n=2000;
for i=1:n:length(Data)
    for j=1:4
        subplot(2,2,j)
        if i+n<length(Data)
            b=plot3(Data(i:i+n,1),Data(i:i+n,2),Data(i:i+n,3),'.','color','black','MarkerSize',0.005);
        else
            b=plot3(Data(i:end,1),Data(i:end,2),Data(i:end,3),'.','color','black','MarkerSize',0.005);
        end            
        uistack(b,'bottom') %you can also do uistack(b,'bottom')
    end
    
    frame=getframe(gcf);
    writeVideo(video,frame)
    %     drawnow
    pause(0.00000000001)
end

close(video)


