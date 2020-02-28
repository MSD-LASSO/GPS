%Author Anthony Iannuzzi, email awi7573@rit.edu
function []=GraphSaver(formats,location,closing,MaximizeAll,plots)
%INPUTS: formats is a cell array of all requested formats. Location is
%where these plots will be saved. plots is an optional input specifying
%what figures to save. 

%    location='Plots\AlongXAxis';
%    formats={'fig','png'};
%    GraphSaver(formats,location,0)

defaultSize=get(0,'defaultfigureposition');
if nargin<4
    MaximizeAll=0;
end
if nargin<5
    plots=1;
end
if exist(location,'dir')==0
    mkdir(location);
end

i=1;
persistance=0; %if there is a gap of 5 figures that don't exist and no figure array was given, stop saving
while i<=length(plots)
    if nargin<5
        plots(i+1)=i+1;
    end
    if ishandle(plots(i))==1
        figure(plots(i))
        h1=gcf;
        [~,el]=view;
        n=length(h1.Children);
        success=0;
        failure=0;
        if n>=3 || el~=90 || MaximizeAll==1 %if figure is a subplot, make it big.
            for j=1:n
                try
                    success=success+1;
                    h2=h1(j).Children;
                    set(h2,'FontSize',18);
                    title=h2.Title;
                    title.FontSize=20;
                catch
                    failure=failure+1;
                end
            end
            if success>=2 || MaximizeAll==1 %then we found 2 Axes.
                set(gcf, 'Position', get(0, 'Screensize'));
            end

        end
        for j=1:length(formats)
            Figtitle=h1.Children(end).Title.String; %take first title for name
            Figtitle=strrep(Figtitle,'.','_');
            Figtitle=strrep(Figtitle,':','_');
            Figtitle=strrep(Figtitle,'/','_');
            try
                saveas(gcf,[location '/' Figtitle],formats{j});
            catch ME
                disp(i)
                rethrow(ME);
            end
            persistance=0;
        end
        if closing==1
            close(h1)
        else
            set(h1,'Position',defaultSize)
        end
    else
        persistance=persistance+1;
        if persistance>5
            break
        end
    end
    i=i+1;
end
        