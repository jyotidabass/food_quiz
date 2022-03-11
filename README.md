# quiz-program
Implementing a text-based quiz program in python using code that communicates with the text file that contains the questions and answers. The code-text file relationship allows for specific syntax to do specific things e.g. stop reading file, start reading answers, in the text file which emulates a programming language.

Text file syntax includes:
<ul>
  <li> $SubjectName - This syntax indicates the start of a quiz of the said subject </li>
  <ul>
    <li>Example usage - Computer Science</li>
    <li>Followed by questions relating to the said subject</li>
  </ul>
  <li> [end question] - Indicates the end of a question</li>
  <li> end ($SubjectName)_quiz - Indicates the end of the quiz of the said subject </li>
  <ul>
    <li> Example usage - end Computer Science_quiz </li>
  </ul>
  <li>($SubjectName)_answers - Indicates start of the answers section of the said subject </li>
  <ul>
    <li> Example usage - Maths_answers </li>
  </ul>
  <li>end ($SubjectName)_answers - Indicates end of the answers section of the said subject </li>
  <ul>
    <li> Example usage - end Maths_answers </li>
  </ul>
  
  
</ul>
