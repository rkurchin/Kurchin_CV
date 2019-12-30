%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CV class file
%
% This template was originally downloaded from:
% http://www.LaTeXTemplates.com
%
% This class file defines the structure and design of the template. 
%
% Original header:
% Copyright (C) 2010 by Trey Hunner
%
% Copying and distribution of this file, with or without modification,
% are permitted in any medium without royalty provided the copyright
% notice and this notice are preserved. This file is offered as-is,
% without any warranty.
%
% Created by Trey Hunner and modified by www.LaTeXTemplates.com, and also by Rachel Kurchin
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ProvidesClass{cv}[2019/12/22 CV class]

\LoadClass[11pt,letterpaper]{article} % Font size, paper

\usepackage[parfill]{parskip} % Remove paragraph indentation


% for the colored lines
\usepackage[dvipsnames]{xcolor}
    \definecolor{CMUred}{cmyk}{0,1,.79,.2}
    \definecolor{CMUdarkgrey}{cmyk}{0,0,0,.7}
    \definecolor{CMUlightgrey}{cmyk}{0,0,0,.3}

\usepackage[left=1.6cm,top=1.4cm,right=1.6cm,bottom=1.6cm]{geometry} % Document margins    
    
%\pagestyle{empty} % To suppress page numbers
\usepackage{fancyhdr} % footer with page number, name
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\color{Gray}Kurchin CV, p. \thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\footskip}{0.5cm}
    
% for email/web links
\usepackage[hidelinks]{hyperref} 
    \hypersetup{
        colorlinks=true,
        linkcolor=blue,
        filecolor=blue,      
        urlcolor=blue
    }

\usepackage{tabularx} % just used in header
\usepackage{longtable} % to make the column on the left with years, etc.

\usepackage{xparse} % fancy interface for defining arguments, defaults, etc. in custom commands/environments

\usepackage{calc} % for arithmetic with lengths

\usepackage{ulem} % consistent underlines

%-----------------------------------------------------
%	HEADINGS COMMANDS: For printing name/address/etc.
%-----------------------------------------------------

% some things for the main document to be more readable
\def \name#1{\def\@name{#1}}
\def \addressone#1{\def\@addressone{#1}}
\def \addresstwo#1{\def\@addresstwo{#1}}
\def \uni#1{\def\@uni{#1}}
\def \dept#1{\def\@dept{#1}}
\def \email#1{\def\@email{#1}}
\def \website#1{\def\@website{#1}}
\def \scholar#1{\def\@scholar{#1}} % Google Scholar link
\def \phone#1{\def\@phone{#1}}

% customizable spacings to get page breaks to work out when adding/removing stuff
\def \sectionfudge#1{\def\@sectionfudge{#1}}
\def \topspace#1{\def\@topspace{#1}}
\def \topfudge#1{\def\@topfudge{#1}}

% for tables later
\newlength\lastwidth
\newlength\firstwidth

\def \printaddress {
  \begingroup
    \begin{tabularx}{\textwidth}{@{} X r @{}}
    \@uni        & \href{mailto:\@email}{\@email} \\
    \@addressone       & \href{https://\@website}{\@website} \\
    \@addresstwo & \href{\@scholar}{Google Scholar} \\
    \end{tabularx}
  \endgroup
  \par
  \vspace{\@topfudge}
}

% \printname is used to print the name as a page header
\def \printname {
  \begingroup
    \nameskip\break
    \noindent  \LARGE{{\textbf{\textsc{\@name}}}} \\
    \vspace{-2ex}
    {\color{CMUred}\hrule height 1.5pt}
    \normalsize
  \endgroup
}


%---------------------------
%	PRINT THE HEADING LINES
%---------------------------

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document  % Begin document
  \printname
  \vspace{1ex}%
  \printaddress
}

%-----------------------
%	SECTION FORMATTING
%-----------------------

% Defines the cvSection environment for the large sections within the CV
% 3 arguments: (required) section name, (optionally) spacing fudge factor and first column width
\NewDocumentEnvironment{cvSection}{m O{-3pt} O{3.37cm}}
{
    \def\@fudgespace{#2}
    \sectionskip
    \MakeUppercase{\bf #1} % Section title
    \sectionlineskip
    {\color{CMUlightgrey}\hrule height 1.5pt}

    % use a table to get the column on the left
    %\setlength\lastwidth{\textwidth-#3}%
    %\begin{longtable}{@{} p{#3} p{\lastwidth}}
    %\setlength\lastwidth{\textwidth-#3}%
    \begin{longtable}{@{} p{#3} p{\textwidth-#3-0.4cm}}
}
{
    \end{longtable}
    \vspace{\@sectionfudge}
}

% define a separate environment for listing pubs
% 3 optional arguments: spacing fudge factor, width of first two columns, and section name (defaults to Publications)
\NewDocumentEnvironment{pubsSection}{O{-3pt} O{2.54cm} O{Publications}}
{
    \def\@fudgespace{#1}
    \sectionskip
    \MakeUppercase{\bf #3} % Section title
    \sectionlineskip
    {\color{CMUlightgrey}\hrule height 1.5pt}

    % use a table to get the column on the left, including a separate column for pub number
    \setlength\firstwidth{#2-0.95cm }
    \begin{longtable}{@{} p{\firstwidth} p{0.6cm} p{\textwidth-#2-0.5cm}}
}
{
    \end{longtable}
    \vspace{\@sectionfudge}
}

% 4 arguments: year, institution, department/location, position
\newcommand{\cvItem}[4] {
    #1 & \textbf{#2} \textit{#3}\\
     & #4\\
     &\\[\@fudgespace]
}

% 3 arguments: year, number, citation
\newcommand{\pubsItem}[3] {
    #1 & [#2] & #3\\
     & & \\[\@fudgespace]
}

% for single-line items with no italics/bold/whatever
% optional first argument allows extra squish, useful for last line
% before a subheader because spacing ends up really big
\newcommand{\lineitem}[3][\@fudgespace] {
    #2 & #3 \\
    &\\[#1]
}

% subheaders, I use in "other skills/activities" section
\newcommand{\subheader}[1] {
    \multicolumn{2}{@{} l}{\uline{\fontsize{13}{14}\selectfont #1}}\\
    &\\[\@fudgespace]
}



% figure out which of these are needed...
\def\sectionlineskip{\medskip} % The space above the horizontal line for each section 
\def\nameskip{\bigskip} % The space after your name at the top
\def\sectionskip{\medskip} % The space after the heading section
