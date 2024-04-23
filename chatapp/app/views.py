from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapter=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Sorry, I dont know what that means',
        'maximum_similarity_threshold': 0.95,
    }
])

list_to_train = [
    "Hi", #question1
    "Hi there!", #answer1
    
    "Hello", 
    "Hello I am EduGuideBot",
    
    "What's your name?",
    "I am EduGuideBot",
    
    "What is your job?",
    "I am here to guide you about IOE Admission",
    
    "What is the full form of IOE?",
    "The full form of IOE is Institute of Engineering",

    "Where is Chitwan Engineering Campups?",
    "It lies in Bharatpur Municipality in Chitwan district.",

    "What program is taught in Chitwan?",
    "Bachelor's in Architecture",

    "What colleges are affiliated to Tribhuwan University?",
    "Kantipur Engineering College, Kathmandu Engineering College, Himalaya Engineering College, Advanced College of Engineering and Management, National College of Engineering, Kathford International College, Janakpur Engineering College, Khwopa College of Engineering, Sagarmatha College of Engineering, Lalitpur Engineering College",

    "Kantipur Engineering College affiliated to Tribhuwan University?",
    "Yes",

    "Kathmandu Engineering College affiliated to Tribhuwan University?",
    "Yes",

    "Himalaya College of Engineering affiliated to Tribhuwan University?",
    "Yes",

    "Advanced College of Engineering affiliated to Tribhuwan University?",
    "Yes",

    "National College of Engineering affiliated to Tribhuwan University?",
    "Yes",

    "Kathford International College of Engineering and Management affiliated to Tribhuwan University?",
    "Yes",

    "Janakpur Engineering College affiliated to Tribhuwan University?",
    "Yes",

    "Khowpa College of Engineering affiliated to Tribhuwan University?",
    "Yes",

    "Sagarmatha Engineering College affiliated to Tribhuwan University?",
    "Yes",

    "Lalitpur Engineering College affiliated to Tribhuwan University?",
    "Yes",

    "Do I need to pass the Entrance Examination conducted by Institute of Engineering to get admission in to the affiliated colleges?",
    "Yes",

    "What are fee programs of the affiliated colleges?",
    "10 percent of the total seats should be enrolled with regular fee.",

    "Pulchowk Campus seats for Civil Engineering?",
    "108 for regular, 84 for full fee",

    "Pulchowk Campus seats for Architecture?",
    "24 for regular, 24 for full fee",

    "Pulchowk Campus seats for Electrical Engineering?",
    "36 for regular, 60 for full fee",

    "Pulchowk Campus seats for Electronics, Communication and Information Engineering?",
    "24 for regular, 24 for full fee",

    "Pulchowk Campus seats for Mechanical Engineering?",
    "24 for regular, 24 for full fee",

    "Pulchowk Campus seats for Computer Engineering?",
    "36 for regular, 60 for full fee",

    "Pulchowk Campus seats for Aerospace Engineering?",
    "12 for regular, 36 for full fee",

    "Pulchowk Campus seats for Agriculture Engineering?",
    "0 for regular, 0 for full fee",

    "Pulchowk Campus seats for Industrial Engineering?",
    "0 for regular, 0 for full fee",

    "Pulchowk Campus seats for Geomatics Engineering?",
    "0 for regular, 0 for full fee",

    "Pulchowk Campus seats for Automobile Engineering?",
    "0 for regular, 0 for full fee",

    "Pulchowk Campus seats for Chemical Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Civil Engineering?",
    "36 for regular, 108 for full fee",

    "Pashimanchal Campus WRC seats for Architecture?",
    "0 for regular, 0 for full fee",

    "Pashimanchal Campus WRC seats for Electrical Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Electronics, Communication and Information Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Mechanical Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Computer Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Aerospace Engineering?",
    "0 for regular, 0 for full fee",

    "Pashimanchal Campus WRC seats for Agriculture Engineering?",
    "0 for regular, 0 for full fee",

    "Pashimanchal Campus WRC seats for Industrial Engineering?",
    "0 for regular, 0 for full fee",

    "Pashimanchal Campus WRC seats for Geomatics Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Automobile Engineering?",
    "12 for regular, 36 for full fee",

    "Pashimanchal Campus WRC seats for Chemical Engineering?",
    "0 for regular, 0 for full fee",

    "Purwanchal Campus ERC seats for Civil Engineering?",
    "36 for regular, 108 for full fee",

    "Purwanchal Campus ERC seats for Architecture?",
    "12 for regular, 36 for full fee",

    "Purwanchal Campus ERC seats for Electrical Engineering?",
    "12 for regular, 36 for full fee",

    "Purwanchal Campus ERC seats for Electronics, Communication and Information Engineering?",
    "12 for regular, 36 for full fee",

    "Purwanchal Campus ERC seats for Mechanical Engineering?",
    "24 for regular, 72 for full fee",

    "Purwanchal Campus ERC seats for Computer Engineering?",
    "24 for regular, 72 for full fee",

    "Purwanchal Campus ERC seats for Aerospace Engineering?",
    "0 for regular, 0 for full fee",

    "Purwanchal Campus ERC seats for Agriculture Engineering?",
    "12 for regular, 36 for full fee",

    "Purwanchal Campus ERC seats for Industrial Engineering?",
    "0 for regular, 0 for full fee",

    "Purwanchal Campus ERC seats for Geomatics Engineering?",
    "0 for regular, 0 for full fee",

    "Purwanchal Campus ERC seats for Automobile Engineering?",
    "0 for regular, 0 for full fee",

    "Purwanchal Campus ERC seats for Chemical Engineering?",
    "0 for regular, 0 for full fee",

    "Thapathali Campus seats for Civil Engineering?",
    "36 for regular, 108 for full fee",

    "Thapathali Campus seats for Architecture?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Electrical Engineering?",
    "0 for regular, 0 for full fee",

    "Thapathali Campus seats for Electronics, Communication and Information Engineering?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Mechanical Engineering?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Computer Engineering?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Aerospace Engineering?",
    "0 for regular, 0 for full fee",

    "Thapathali Campus seats for Agriculture Engineering?",
    "0 for regular, 0 for full fee",

    "Thapathali Campus seats for Industrial Engineering?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Geomatics Engineering?",
    "0 for regular, 0 for full fee",

    "Thapathali Campus seats for Automobile Engineering?",
    "12 for regular, 36 for full fee",

    "Thapathali Campus seats for Chemical Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Civil Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Architecture?",
    "6 for regular, 18 for full fee",

    "Chitwan Campus seats for Electrical Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Electronics, Communication and Information Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Mechanical Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Computer Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Aerospace Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Agriculture Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Industrial Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Geomatics Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Automobile Engineering?",
    "0 for regular, 0 for full fee",

    "Chitwan Campus seats for Chemical Engineering?",
    "0 for regular, 0 for full fee",

    "Seats in Kantipur Engineering College for Civil Engineering",
    "96",

    "Seats in Kantipur Engineering College for Architecture",
    "0",

    "Seats in Kantipur Engineering College for Electrical Engineering",
    "0",

    "Seats in Kantipur Engineering College for Electronics, Communication and Information Engineering",
    "96",

    "Seats in Kantipur Engineering College for Computer Engineering",
    "96",

    "Seats in Kathmandu Engineering College for Civil Engineering",
    "96",

    "Seats in Kathmandu Engineering College for Architecture",
    "48",

    "Seats in Kathmandu Engineering College for Electrical Engineering",
    "48",

    "Seats in Kathmandu Engineering College for Electronics, Communication and Information Engineering",
    "96",

    "Seats in Kathmandu Engineering College for Computer Engineering",
    "96",

    "Seats in Himalaya Engineering College for Civil Engineering",
    "96",

    "Seats in Himalaya Engineering College for Architecture",
    "48",

    "Seats in Himalaya Engineering College for Electrical Engineering",
    "0",

    "Seats in Himalaya Engineering College for Electronics, Communication and Information Engineering",
    "48",

    "Seats in Himalaya Engineering College for Computer Engineering",
    "48",

    "Seats in Advanced College of Engineering for Civil Engineering",
    "96",

    "Seats in Advanced College of Engineering for Architecture",
    "0",

    "Seats in Advanced College of Engineering for Electrical Engineering",
    "48",

    "Seats in Advanced College of Engineering for Electronics, Communication and Information Engineering",
    "96",

    "Seats in Advanced College of Engineering for Computer Engineering",
    "96",

    "Seats in National College of Engineering for Civil Engineering",
    "96",

    "Seats in National College of Engineering for Architecture",
    "0",

    "Seats in National College of Engineering for Electrical Engineering",
    "48",

    "Seats in National College of Engineering for Electronics, Communication and Information Engineering",
    "48",

    "Seats in National College of Engineering for Computer Engineering",
    "48",

    "Seats in Kathford Internationl College of Engineering for Civil Engineering",
    "96",

    "Seats in Kathford Internationl College of Engineering for Architecture",
    "0",

    "Seats in Kathford Internationl College of Engineering for Electrical Engineering",
    "0",

    "Seats in Kathford Internationl College of Engineering for Electronics, Communication and Information Engineering",
    "48",

    "Seats in Kathford Internationl College of Engineering for Computer Engineering",
    "48",

    "Seats in Janakpur Engineering College for Civil Engineering",
    "96",

    "Seats in Janakpur Engineering College for Architecture",
    "0",

    "Seats in Janakpur Engineering College for Electrical Engineering",
    "0",

    "Seats in Janakpur Engineering College for Electronics, Communication and Information Engineering",
    "48",

    "Seats in Janakpur Engineering College for Computer Engineering",
    "48",

    "Seats in Khowpa College of Engineering for Civil Engineering",
    "96",

    "Seats in Khowpa College of Engineering for Architecture",
    "0",

    "Seats in Khowpa College of Engineering for Electrical Engineering",
    "48",

    "Seats in Khowpa College of Engineering for Electronics, Communication and Information Engineering",
    "0",

    "Seats in Khowpa College of Engineering for Computer Engineering",
    "48",

    "Seats in Sagarmatha Engineering College for Civil Engineering",
    "48",

    "Seats in Sagarmatha Engineering College for Architecture",
    "0",

    "Seats in Sagarmatha Engineering College for Electrical Engineering",
    "0",

    "Seats in Sagarmatha Engineering College for Electronics, Communication and Information Engineering",
    "48",

    "Seats in Sagarmatha Engineering College for Computer Engineering",
    "48",

    "Seats in Lalitpur Engineering College for Civil Engineering",
    "48",

    "Seats in Lalitpur Engineering College for Architecture",
    "0",

    "Seats in Lalitpur Engineering College for Electrical Engineering",
    "0",

    "Seats in Lalitpur Engineering College for Electronics, Communication and Information Engineering",
    "0",

    "Seats in Lalitpur Engineering College for Computer Engineering",
    "48",

    "What happens if the program is postponed after I've already paid the admission fee?",
    " If the program is postponed, the campus will refund your admission fee in full.",

    "Can I still apply for the program even if it's postponed?",
    "If the program is postponed, you won't be able to enroll in it for that year. However, you can consider applying for other programs or waiting to see if the program is offered in subsequent years.",

    " How will I know if the program is being postponed?",
    "The campus will communicate any decision to postpone a program through official channels, such as the website or email. You should regularly check for updates regarding the status of the program.",

    "Will I be able to get admission into another program if the one I applied for is postponed?",
    "Yes, you can explore other programs offered by the campus and apply accordingly. Your application for the postponed program won't affect your eligibility for other programs.",

    "What does it mean to transfer from the full-fee side to the regular side?",
    "Transferring from the full-fee side to the regular side means that students who initially paid the full fee to secure admission will be transferred to the regular side once the full-fee quota is filled. This allows students to switch to the regular quota without any additional cost.",

    "How will I know if I'm eligible for transfer to the regular side?",
    " Eligibility for transfer to the regular side will be based on merit order. Once the full-fee quota is filled, students will be transferred to the regular side according to their merit ranking.",

    " What happens if I've already paid the full fee but get transferred to the regular side?",
    "If you've already paid the full fee but are transferred to the regular side, you may be eligible for a refund of the difference between the full fee and the regular fee. The campus will provide guidance on the refund process.",

    "What is the difference between regular admission and full-fee admission?",
    "Regular admission entails paying the minimum tuition fees, while full-fee admission allows applicants to secure admission by paying higher fees.",

    "How are applicants admitted to the graduate (B.E./B.Arch.) level programs at the Institute of Engineering campuses?",
    "Applicants interested in studying at Pulchok Campus, Western Campus, Purvanchal Campus, Thapathali Campus, Chitwan Engineering Campus, and affiliated colleges must take the entrance exam conducted by the Institute of Engineering Studies. Admission is based on merit, determined by the entrance exam scores.",

    "What are the minimum qualifications required to apply for the entrance examination?",
    "Applicants must have obtained at least 45 percent of the total marks in the proficiency certificate level, higher secondary level, A level, or engineering diploma level examinations, with physics, chemistry, and mathematics as subjects. Alternatively, students who have obtained a minimum C Grade in each subject or have appeared in the final examination of class 12 or engineering diploma sixth-semester examination are also eligible to apply.",

    " Can students with a letter grading system apply for the entrance examination?",
    " Yes, students with a letter grading system can apply for the entrance examination if they have obtained a minimum C Grade in each subject.",

    "Are there any specific subject requirements for the entrance examination?",
    "Yes, applicants must have studied physics, chemistry, and mathematics in classes 11 and 12 or equivalent levels to be eligible for the entrance examination.",

    " Are there any exceptions to the minimum qualifications for application?",
    "Exceptions are made for students who have appeared in the final examination of class 12 or equivalent or have appeared in the sixth-semester examination of an engineering diploma program.",

    "Can applicants from educational institutions outside the country apply for the entrance examination?",
    "Yes, applicants who have completed their education from educational institutions recognized by the Vidya Parishad are eligible to apply for the entrance examination, provided they meet the minimum qualification criteria.",

    "What method will be used for conducting the entrance examination?",
    "The entrance examination will be conducted through a computer examination system based on information technology, ensuring a standardized and efficient assessment process.",

    "Who will be responsible for conducting the entrance examination?",
    "The entrance examination will be conducted by the board responsible for administering admissions to the graduate (B.E./B.Arch.) level programs.",

    " How much weightage will the entrance exam results carry in the admission process?",
    "The results of the entrance examination will carry 100 percent weightage in determining the eligibility of applicants for admission to the campus based on merit.",

    "What subjects will be covered in the entrance examination?",
    "The entrance examination will cover four subjects: Mathematics, Physics, Chemistry, and English, based on the 10+2 level syllabus.",

    "How long will the entrance examination last?",
    "The duration of the entrance examination, conducted through a fully computerized examination system, will be two hours. Additionally, there will be a penalty of deducting 10% marks for each wrong answer.",

    "What documents are required for filling the online admission form and appearing for the entrance exam?",
    "Applicants must bring a color-printed admit card and upload proof of identification documents (such as Citizenship Certificate, National Identity Card, Passport, Driver's License, or relevant academic certificates) when filling the online admission form. These documents must also be presented during the entrance examination for verification purposes.",

    "How will the entrance examination results be evaluated and presented?",
    "The entrance score will be calculated as a percentage of the total score of the entrance exam. A merit list of candidates who have obtained the minimum passing percentage or above will be published on the website entrance.ioe.edu.np.",

    " Where can I find information about admission-related procedures and activities?",
    "Information about admission-related work can be obtained from the web address of the Central Admission Committee: admission.ioe.edu.np, as well as from the websites of related campuses and colleges.",

    "How will candidates be selected for admission based on merit?",
    " Merit list for admission will be published based on the entrance score, with candidates who have obtained the minimum marks percentage or more in the entrance examination being included. In case of equality in scores, priority will be given to candidates based on certain criteria, including subject-wise scores and previous academic performance.",

    "What happens if two or more candidates have the same entrance score?",
    "In case of equality in entrance scores, priority will be determined by calculating the total result to three decimal places. If scores are still equal, preference will be given to the candidate with higher marks in Mathematics, Physics, Chemistry, and English subjects. Subsequently, preference will be given to the candidate with higher scores in their 10+2 or equivalent and SLC/SEE exams, respectively.",

    "Will the merit list be published in a specific order?",
    "Yes, the merit list will be published in a specific order based on the criteria mentioned above, ensuring transparency and fairness in the selection process.",

    "How will the admission list be published for affiliated campuses and colleges under the Institute of Engineering Studies?",
    "The admission list publication and admission process for affiliated campuses and colleges will be centralized under the Institute of Engineering Studies. The lists will be published by the Monitoring Committee and can be viewed later at admission.ioe.edu.np for reference.",

    "What is the process for admission according to the admission schedule?",
    "According to the admission schedule published by the Central Admission Monitoring Committee, respective campuses/colleges will publish the admission list in merit order based on the names published in the merit list by the Entrance Examination Board. Applicants for the architecture program may also need to take an aptitude test related to the subject.",

    " How are applicants selected for admission in reserved quotas for affiliated campuses of TU?",
    "Names of applicants who apply for admission in any reserved quota for affiliated campuses of TU will be published based on merit only during the first stage admission program (first, second, and third lists). However, applicants admitted in the reserved quota in one campus cannot be readmitted in the reserved quota in another campus.",

    "Will there be any additional tests for applicants applying for the architecture program?",
    " Yes, applicants whose names have been published for admission to the architecture program may be required to take an aptitude test (Aptitude Test) related to that subject by the respective campuses/colleges.",

    "What are the documents required for the further admission process?",
    "If you are eligible for admission in the college you will to provide the following documents to the adminstration in the given date i) SEE certificate or equivalent certificate from recognized board along with the character certificate (original and photocopy each) ii) +2 certificate from educational institute recognized by NEB with science background , A level or engineering diploma or equivalent exam  with minimum of 45 percent and incase of letter grading the candidate should have final grade C along with the transcript and character certificate ( original and photocopy each) iii) Nepali citizenship ( original and photocopy each ) iv) If your college is not recognized by the NEB then you should also provide the migration certificate from the institution you completed your high school degree ( original and photocopy each )",

    "What if you are a foreign student ?",
    "If you are foreign student then you should bring your passport with you as well but if you are from india you can just provide the identification card provided by the embassy.",

    "Are there any quotas ?",
    "Yes, there is some quotas for the people from the different background. You can see the detail about it in our website.",

    "What if there are some mistakes in the documents provided ?",
    "If the provided documents contain faulty information or the requirements for the admission such as grades doesn't fulfill accordingly then the admission is terminated, even if the candidate name is already published.",

    "Do I have to be present on the class at the start of the session ?",
    "Yes, you should be present in the classroom for atleast once during the 1st week of the session otherwise your name will be dismissed from the admission list and the seat will be given to the students according to the priority list.",

    "Can i cancel my admission ?",
    "Yes, you can.",

    "If i cancel my admission do i get a refund ?",
    "It depends. If you cancel the admission admission before the start of the session then you will get refund upto 80 percent , if you cancel the admission within a week of the start of the session then you will be refunded upto 50 percent and if you cancel the admission after a week of the start of the session then unfortunately you will not be refunded.",

    "What will happen to the security money that is deposited?",
    "If you complete your bachelor's degree under the same university then the security deposit will be handed to you within a year after your graduation.",

    "What if I don't complete my undergraduate degree and leave the college. Do i still get the security money?",
    "No, If due to some reason you are unable to continue your study and if you leave the college then the security money will not be handed to you.",

    "Do i have to regularly study for 4 years or do i get to take a gap?",
    "You can take a gap in the study within the 4 years and can continue studying in the same college provided that there is a vacant seat available. Also you have to inform you respective college beforehand if want to rejoin the college.",

    "Does all the  affiliated college under TU has same rules and regulation?",
    "Yes, with some minor changes all the college under TU has same guidance you need to follow.",

    "Is there a library in the college?",
    "Yes, there is a big library in the college which you can access with the help of your identification card.",

    "What is the estimated cost of studying in Pulchowk campus?",
    "Depends. If you are a regular student then your tution fee will be around Rs.5000 per semester and if you are full fee student then your tution feel will be around Rs.32500 per semester. Remember this is the rough estimation.",

    "Does the cost of studying in pulchowk campus increases yearly?",
    "Yes , There is a certain percentage growth in the tution fee each year but the enrolled students are uneffected by this growth.",

    "Is there a hostel in Pulchowk campus ?",
    "Yes, The campus provide the hostel facility to the selected students ( based on the merit list) . It will require you to fill the another form and will require certain criteria well that will be listed in the form.",

    "How are exams conducted in the pulchowk campus ?",
    "Exams in the pulchowk campus or as a matter of fact for any university under TU are conducted on a semiannually basis ( within 6 months )",

    "How do i get access to my identification card ?",
    "If you are admitted to the college then you will be provided with your identication card on your first day.",

    "How many seats are there in pulchowk campus?",
    "There are total of 625 seats allocated to different programs.",

    "How many written exams do i have to give each semester ?",
    "You will have internal exams for each subject in the semester and final exams as well for each carrying most 20 marks and 80 marks respectively. Some subjects might have less marking related to their credit hour.You need to have admit card to attend the exams.",

    "Do i have to fill out the exam form for internal exams as well?",
    "No, you don't need to fill out the exam form or have an admit card to give internal exams.",

    "Do i have to fill out exam form for each semester exam?",
    "Yes, You need to fill the exam form each semester exam and failing to do so will make you ineligible to attend the further exams.",

    "Is there any schedule for the condution of exams or events or holidays ?",
    "Yes,  There is a IOE calendar where you can look up the exams dates or events and other programs that are held by college officially.",

    "What is the attendance policy ?",
    "You are Strictly require to have atleast 75 percent attendance to be eligible for final exam and failing to meet the above requirement can effect you academically.",

    "How many books can i borrow from library ?",
    "You can borrow atmost 7 books from the library which are needed to be renewed again and again after 90 days , failing to do so will result in fine of Re.1 for each book for single day.",

    "Is there a provision for scholorship ?",
    "Yes, There are various provision for scholorship which will be provided to you based on your academic performances.",

    "What if I fail in the internal exam?",
    "If you fail in your internal exam , you need to do some coursework provided by your subject teacher to be eligibile to sit in the Semester exam.",

    "What if I fail in Semester exam?",
    "In an unfortunate case, if you fail in semester exam then you can give back exam for the subject according to the routine that will be provided to you. You need to fill out the form as well to give back exam with the back fee of Rs.1100.The back exam will be conducted yearly.",

    "What is the dress code for the pulchowk college?",
    "There is not strict dress code and you are not obliged to wear any specific dress inside college but it would be unethical for students to dress improperly.",

    "Do I have to be present on the day of admission?",
    "Yes, It is compulsory for the candidate to be present at the time of admission along with their guardian.",

    "Can I switch from one instituent college to another ?",
    "It depends.If there are no available seats in the college you want to switch then you cannot switch. Even if there are available seats in the college you would require to fill out the form for the college during the time of admission.In conclusion, It would not be upto you to take the decision to switch the college. If there are available seats in other college you would be informed accordingly if you want to switch.",

    "How would I get the Mails from college?",
    "You will be provided with the college Mail which will be used to interact with you.",

    "How do I pay for the semester fee ?",
    "When you are admitted to the college , you will also be required to open a bank account with Siddartha Bank. Any financial transaction between you and college would be through the same Bank account. To deposit your semester fee , you will be needed to deposit the required amount in the provided bank account and college adminstration will deduce the tution fee accordingly.",

    "Is there a transportation facility for students ?",
    "Unfortunately , There is no transportation service provided by the college and Student need to manage the transportation by themselves.",

    "What if I am unable to clear my exams within 4 years?",
    "In such unfortunate case, You will have next four years to complete all your back exams.So in total you will actually have total 8 years to complete your Engineering degree.",

    "What is the college hour in pulchowk campus?",
    "In summer , Typical college hour is from 10:15 am to 5:00 pm. In winter, It ranges from 10:15 am to 4:00 pm.",

    "How are admission date decided?",
    "Admission date are decided according to the program that you are enrolled.For example If an admission date is allocated for certain day then there is an enrollment for certain program only for that day.If for some reason , you missed the your admission then there is a provision to fill out the admission form again once all the program's enrollment are completed.",

    "Do I get to change the major during the 4 year?",
    "No, Once you are enrolled in a certain program you are obliged to complete the undergraduate course in same program.",

    "Do I get to choose more than one major ?",
    "No, you can be enrolled in one and only undergraduate program.",

    "How are my transcripts and certificates are used by the college?",
    "Your transcripts and certificates are not used by the college by any means and are kept safely as a collateral and will be provided to you after you complete your undergraduate program.",

    "Is there no provision for online admission ?",
    "Unfortunately No, Candidates are required to visit the college adminstration for the further admission process.",

    "What are the provisions for extra curricular activites ?",
    "There are various programs and sport events organized within the college.Even though there is no direct involvement of college adminstration in the programs and events , college will help the students to organize such programs.",

    "What are the medical services provided by the college?",
    "There are medical staff in college where students will be supervised by the professionals in the time of urgency or health problems.",

    "Can i get suspended from college?",
    "Yes , If the college adminstration believe you are guilty of charged allegations such as extremely inappropirate behaviour then you will be punished accordingly. You can be suspended from 3 to 15 days and if the charged allegation is extreme enough you can be restricted as well.",

    "How would i know about the routines for each day?",
    "There is a notive board in the adminstration where the notices and routines are updated in time. You can visit there to look at the notice or it will be provided by the selected Class Representative ( CR ).",

    "How do I apply for the reserved quota?",
    "If you are eligible to apply the reserved quota you can fill out the form according to the information provided in our website with required documents.",

    "Am i eligible for regular scholorship If i don't have nepali citizenship?",
    "If you do not own nepali citizenship then you have to apply for the college through foreign quota. The tution fee for foreign student is enlisted in the websited.So even if you are eligible for regular scholorship , without nepali citizenship you will be required to enroll in the college through foregin quota in full fee.",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'app/index.html')

def specific(request):
    return HttpResponse("number")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    while chatResponse == "":
        chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)