import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# 제목 설정
st.title("육하원칙 기반 작문 도우미")

# API 키 입력
api_key = st.text_input("Google API Key를 입력하세요", type="password")

# 육하원칙 입력 필드
who = st.text_input("누가 (Who)")
what = st.text_input("무엇을 (What)")
when = st.text_input("언제 (When)")
where = st.text_input("어디서 (Where)")
why = st.text_input("왜 (Why)")
how = st.text_input("어떻게 (How)")

# 프롬프트 템플릿 작성
template = """다음의 육하원칙을 기반으로 자연스러운 글을 작성해주세요:

누가: {who}
무엇을: {what}
언제: {when}
어디서: {where}
왜: {why}
어떻게: {how}

위 정보를 바탕으로 자연스럽게 연결된 하나의 글을 작성해주세요. 
문장이 매끄럽게 이어지도록 해주시고, 필요한 경우 적절한 접속사나 부연 설명을 추가해주세요."""

prompt = PromptTemplate(
    input_variables=["who", "what", "when", "where", "why", "how"],
    template=template
)

# 생성 버튼
if st.button("글 생성하기"):
    if not api_key:
        st.error("API 키를 입력해주세요!")
    elif not all([who, what, when, where, why, how]):
        st.warning("모든 항목을 입력해주세요!")
    else:
        try:
            # Gemini 모델 초기화
            llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
            
            # 프롬프트 생성 및 실행
            final_prompt = prompt.format(
                who=who,
                what=what,
                when=when,
                where=where,
                why=why,
                how=how
            )
            
            # 결과 생성
            response = llm.invoke(final_prompt)
            
            # 결과 출력
            st.subheader("생성된 글:")
            st.write(response.content)
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")

