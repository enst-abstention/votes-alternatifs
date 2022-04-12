import { TranslatableClassicVoteCandidatesList } from "./ClassicVoteCandidatesList.mjs"; // FIXME: We have to import TranslatableClassicVoteCandidatesList instead of ClassicVoteCandidatesList, because otherwise Storybook throws a hook error.
import { TranslatableMajorityJudgmentVoteCandidatesList } from "./MajorityJudgmentVoteCandidatesList.mjs";
import { TranslatablePreferentialVotingCandidatesList } from "./PreferentialVotingCandidatesList.mjs";
import { QuestionTypeEnum, detectQuestionType } from "../election_utils.mjs";

function TranslatableQuestionWithVotableAnswers({ questionType, minimumAnswers, maximumAnswers, question, answers, blankVoteIsAllowed, identifierPrefix, visible, currentUserVoteForQuestion, currentAlertsTextsForQuestion, currentCandidatesHavingAlertsForQuestion, dispatchUpdateUserVoteForQuestion, availableGrades=null, t }){
  let description;
  let rendered_answers;
  if (questionType === QuestionTypeEnum.MAJORITY_JUDGMENT){
    description = t("majority_judgment_question_description");
    rendered_answers = e(
      TranslatableMajorityJudgmentVoteCandidatesList,
      {
        identifierPrefix,
        candidates: answers,
        blankVoteIsAllowed,
        availableGrades,
        currentUserVoteForQuestion,
        currentCandidatesHavingAlertsForQuestion,
        dispatchUpdateUserVoteForQuestion,
        t
      }
    );
  }
  else if (questionType === QuestionTypeEnum.PREFERENTIAL_VOTING){
    description = t("preferential_voting_question_description");
    rendered_answers = e(
      TranslatablePreferentialVotingCandidatesList,
      {
        identifierPrefix,
        candidates: answers,
        blankVoteIsAllowed,
        currentUserVoteForQuestion,
        currentCandidatesHavingAlertsForQuestion,
        dispatchUpdateUserVoteForQuestion,
        t
      }
    );
  }
  else if (questionType === QuestionTypeEnum.CLASSIC){
    let classic_question_subtype = "checkbox";
    if ( minimumAnswers === 1 && maximumAnswers === 1){
      classic_question_subtype = "radio";
    }
    if ( minimumAnswers === maximumAnswers ){
      description = t("ask_to_select_x_answers", {count: minimumAnswers});
    }
    else {
      description = t("ask_to_select_between_x_and_y_answers", {min: minimumAnswers, count: maximumAnswers});
    }
    rendered_answers = e(
      TranslatableClassicVoteCandidatesList,
      {
        type: classic_question_subtype,
        identifierPrefix,
        candidates: answers,
        blankVoteIsAllowed,
        currentUserVoteForQuestion,
        currentCandidatesHavingAlertsForQuestion,
        dispatchUpdateUserVoteForQuestion,
        t
      }
    );
  }
  const bemBlockName = "question-with-votable-answers";
  const containerClassNames = visible ? bemBlockName : `${bemBlockName} ${bemBlockName}--hidden`;
  const alertsElements = currentAlertsTextsForQuestion.reduce(
    (accumulator, value) => {
      if (value){
        accumulator.push(e('p', null, value));
      }
      return accumulator;
    },
    []
  );
  return e(
    'div',
    {
      className: containerClassNames
    },
    e(
      "h3",
      {
        className: `${bemBlockName}__question-title`
      },
      question
    ),
    e(
      "p",
      {
        className: `${bemBlockName}__question-description`
      },
      description
    ),
    rendered_answers,
    e(
      "div",
      {
        className: `${bemBlockName}__alerts`
      },
      ...alertsElements
    )
  );
}

TranslatableQuestionWithVotableAnswers.defaultProps = {
  "questionType": QuestionTypeEnum.CLASSIC,
  "answers": [
    "Answer 1",
    "Answer 2",
    "Answer 3"
  ],
  "minimumAnswers": 1,
  "maximumAnswers": 2,
  "blankVoteIsAllowed": false,
  "question": "Question 1?",
  "identifierPrefix": "question_1_",
  "visible": true,
  "currentUserVoteForQuestion": [],
  "currentAlertsTextsForQuestion": [],
  "currentCandidatesHavingAlertsForQuestion": [],
  "dispatchUpdateUserVoteForQuestion": () => {}
};

const QuestionWithVotableAnswers = ReactI18next.withTranslation()(TranslatableQuestionWithVotableAnswers);

export { QuestionWithVotableAnswers, TranslatableQuestionWithVotableAnswers };
export default QuestionWithVotableAnswers;
