import database
import workflow


def main():
    # إنشاء قاعدة البيانات
    database.init_db()

    # إضافة تقييم تجريبي
    workflow.save_cv_evaluation(
        user_id=1,
        cv_text="This is a sample CV text",
        score=90.0,
        feedback="Strong CV",
        date="2026-07-22"
    )

    print("✅ Database initialized successfully.")
    print("✅ Sample evaluation saved successfully.\n")

    # عرض جميع التقييمات
    evaluations = workflow.get_all_cv_evaluations()

    print("========== CV Evaluations ==========\n")

    if evaluations:
        for evaluation in evaluations:
            print(evaluation)
    else:
        print("No evaluations found.")


if __name__ == "__main__":
    main()