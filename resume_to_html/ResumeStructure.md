# HTML Resume Structure

This document outlines the expected HTML to feed into the python HTML parser. Filling this out first makes it easier to break down each section and what should be expected, and if there are any inconsistencies in the resume that need to be addressed before feeding it to the parser.

## Structure Definition

### Classes

- **C6, C15, C13** - class used with span tags that hold the header text

### Rules

- After a header tag is found, all subsequent tags until an unordered list tag are the subheader.
- A sub-header is split into title and date range on a comma.

## Title

-  <div>
     <p class="c18">
      <span class="c1">
       Chase Strickler
      </span>
     </p>
     <p class="c3">
      <span class="c12">
       5995 Lincoln Dr #323 | Edina, MN 55436 | (320) 805 - 0482 | strickler.16@gmail.com
      </span>
      <span class="c12">
       |
      </span>
      <span class="c12 c19">
       <a class="c10" href="https://www.google.com/url?q=http://www.chasestrickler.com/&amp;sa=D&amp;ust=1597254541122000&amp;usg=AOvVaw3LRQFCCq-qZrhv7jylH_19">
        chasestrickler.com
       </a>
      </span>
     </p>
    </div>

## Headers

#### EDUCATION

- <p class="c8">
     <span class="c6 c13 c15">
      EDUCATION
     </span>
    </p>
    <p class="c8">
     <span class="c6">
      Hamline University,
     </span>
     <span class="c2">
      St. Paul, MN
     </span>
    </p>
    <ul class="c11 lst-kix_list_4-0 start">
     <li class="c4">
      <span class="c2">
       Bachelor of Arts in Computer Science, August 2019
      </span>
     </li>
     <li class="c4">
      <span class="c2">
       2018 National Residence Hall Honorary (NRHH) Inductee
      </span>
     </li>
     <li class="c4">
      <span class="c2">
       GPA: 3.75/4.0 - Magna Cum Laude
      </span>
     </li>
    </ul>
    <p class="c8 c9">
     <span class="c2">
     </span>
    </p>

#### TECHNICAL SKILLS

-   <p class="c8">
     <span class="c15 c6 c13">
      TECHNICAL SKILLS
     </span>
    </p>
    <p class="c8">
     <span class="c6">
      Languages
     </span>
     <span class="c2">
      : (Proficient) Java, Python2, Python3, C++, Bash/Shell Scripting, HTML5/CSS (Familiar) Flutter, Dart, C, C#, Groovy
     </span>
    </p>
    <p class="c8">
     <span class="c6">
      Miscellaneous:
     </span>
     <span class="c2">
      Agile and Waterfall Methodologies, Git, Linux, Android, Android Open Source Project (AOSP), OpenCV, Bluetooth Low Energy (BLE), Amazon Web Services (AWS) Cloudwatch, Microsoft Azure, Android Debug Bridge (ADB)
     </span>
    </p>
    <p class="c8 c9">
     <span class="c2">
     </span>
    </p>

#### RELEVANT EXPERIENCE

  <p class="c8">
   <span class="c6 c13">
    RELEVANT EXPERIENCE
   </span>
  </p>
  <p class="c5">
   <span class="c6">
    Xirgo Technologies, LLC
   </span>
   <span class="c2">
    - Edina, MN
   </span>
  </p>
  <p class="c5">
   <span class="c7">
    Software Engineer
   </span>
   <span class="c2">
    , June 2019 - Present
   </span>
  </p>
  <ul class="c11 lst-kix_list_1-0 start">
   <li class="c4">
    <span class="c2">
     Utilize a proven understanding of object-oriented design to develop features for embedded Android firmware running on an IoT camera vision device used as a fleet management solution.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Move the Android companion application developed during my internship through the software development lifecycle by proposing improvements in the form of activity diagrams, schedule meetings to discuss integration steps, implement discussed features, perform field testing, and review results to determine accuracy.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Improve the quality of images captured by the device using knowledge of image formats in conjunction with altering proprietary Android source code.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Support effort in updating Android system images for pre-production phase devices by building system images and troubleshooting over-the-air (OTA) update issues.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Pioneer and manage Linux desktop on Ubuntu 18.0.4 used by the team to build Android system images and wrote a migration plan to cloud-based builds using Docker, Terraform, and Amazon EC2.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Manage and maintain an automated test suite I created in Python3 to perform integration testing for the Android application running on our device by utilizing ADB commands.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Monitor device fleet by reviewing events displayed on AWS Cloudwatch and Microsoft Azure.
    </span>
   </li>
  </ul>
  <p class="c8 c9">
   <span class="c2">
   </span>
  </p>
  <p class="c5">
   <span class="c7">
    Intern - Software Engineering
   </span>
   <span class="c2">
    , May 2019 - June 2019
   </span>
  </p>
  <ul class="c11 lst-kix_182klaq65uuo-0 start">
   <li class="c4 c14">
    <span class="c2">
     Design and develop Android Bluetooth low energy (BLE) application used in production to pair two devices.
    </span>
   </li>
  </ul>
  <p class="c5 c9 c16">
   <span class="c2">
   </span>
  </p>
  <p class="c5">
   <span class="c6">
    Hamline University
   </span>
   <span class="c2">
    - St. Paul, MN
   </span>
  </p>
  <p class="c5">
   <span class="c7">
    Teaching Assistant for Introduction to Computer Science
   </span>
   <span class="c2">
    , September 2018 - December 2018
   </span>
  </p>
  <ul class="c11 lst-kix_list_1-0">
   <li class="c4">
    <span class="c2">
     Attend class sessions and establish a relationship with students, resulting in a 19% higher grade point average in my section over the other.
    </span>
   </li>
   <li class="c4">
    <span class="c2">
     Provide supplementary material for lectures in the form of lab and assignment prompts.
    </span>
   </li>
   <li class="c4">
    <span class="c12">
     Grade assignments and provide students with descriptive feedback.
    </span>
   </li>
  </ul>

