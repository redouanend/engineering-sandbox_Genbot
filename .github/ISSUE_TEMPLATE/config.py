from mistralai import Mistral

API_KEY = "fOTxUhR9dDPIsmNOCRIxggr0Erhew4yk"  # a encoder avant git

client = Mistral(api_key=API_KEY)

MODEL = "mistral-small"

system_prompt = """
Tu es GenBot, un assistant conçu pour répondre aux questions concernants l'association Génération IA.
Tu réponds uniquement à partir de la knowledge base fournie.
Si la réponse n'est pas dans la base, dis que tu invites l'interlocuteur à contacter directement l'association à partir de la rubrique Contact.
Le chatbot de Génération IA doit répondre de manière claire, pédagogique et bienveillante.
Il doit éviter le jargon technique sauf si l’utilisateur le demande explicitement.
Il doit rediriger vers un contact humain lorsque la demande dépasse son périmètre.
Il doit aller droit au but lorsqu'une question est posée et développer quand c'est nécéssaire.

Le chatbot ne remplace pas un conseiller humain pour les demandes spécifiques ou complexes.
"""

knowledge_base = """
[Génération IA est une association dédiée à la sensibilisation à l’intelligence artificielle.

Sa mission principale est de démocratiser l’IA, d’expliquer ses usages, ses opportunités et ses limites, et de favoriser une utilisation responsable et éclairée de l’intelligence artificielle.

Génération IA s’adresse à un public large, notamment les étudiants, les entreprises, les professionnels, le grand public, les institutions et toute personne curieuse de découvrir l’intelligence artificielle.

L’association met l’accent sur la pédagogie, l’accessibilité et l’éthique de l’IA.

Génération IA défend une vision de l’intelligence artificielle accessible à tous, compréhensible même sans background technique, utilisée de manière responsable et éthique, et pensée comme un outil au service de l’humain et de la société.

L’association encourage l’esprit critique face aux technologies d’IA, la compréhension des enjeux sociaux, sociétaux et environnementaux, ainsi que la transmission de connaissances de manière simple, concrète et pédagogique.

Génération IA propose des formations et des ateliers autour de l’intelligence artificielle.

Ces formations peuvent inclure une initiation à l’intelligence artificielle, la compréhension du fonctionnement des modèles d’IA, des cas d’usage concrets, des applications de l’IA dans le monde professionnel, ainsi que des thématiques liées à l’IA et à l’éthique.

Les formats proposés peuvent être des ateliers interactifs, des conférences ou des workshops pratiques.

Les formations s’adressent à différents publics, notamment les débutants, les étudiants, les professionnels et les entreprises.

Les interventions peuvent avoir lieu en présentiel, en distanciel ou être conçues sur mesure pour les entreprises.

La durée des formations est variable selon les besoins des institutions, les ateliers destinés aux collégiens et lycées sont généralement de 2h.

Génération IA accompagne également les entreprises dans la compréhension et l’adoption de l’intelligence artificielle.

Les objectifs de cet accompagnement sont de démystifier l’IA, de présenter des cas d’usage concrets, d’expliquer les opportunités et les limites de l’intelligence artificielle, et de sensibiliser aux enjeux éthiques et réglementaires.

Les interventions sont adaptées au secteur d’activité de l’entreprise, à son niveau de maturité en intelligence artificielle et à ses besoins spécifiques.

Génération IA participe et initie des projets en lien avec l’intelligence artificielle.

Ces projets peuvent être éducatifs, associatifs, expérimentaux ou réalisés en partenariat avec des entreprises ou des institutions.

Ils visent à appliquer l’IA à des problématiques concrètes, à développer des compétences techniques et humaines, et à promouvoir une intelligence artificielle utile et responsable.

Génération IA organise régulièrement des événements autour de l’intelligence artificielle.

Ces événements peuvent prendre la forme de conférences, d’ateliers, de tables rondes ou de moments d’échange autour des enjeux de l’IA.

Les informations à jour concernant les événements sont disponibles sur le site web et les réseaux sociaux de Génération IA.

Génération IA s’adresse notamment aux étudiants, aux entreprises, au grand public et aux bénévoles.

Pour les étudiants, l’association permet de découvrir l’intelligence artificielle, de mieux comprendre les métiers liés à l’IA, de participer à des projets et de développer de nouvelles compétences.

Pour les entreprises, Génération IA propose des actions de sensibilisation, de formation et d’accompagnement à travers notamment des Team Building, afin de mieux comprendre les enjeux stratégiques et éthiques de l’intelligence artificielle.

Pour le grand public, l’association vise à vulgariser l’IA, à répondre aux idées reçues et à expliquer l’impact de l’intelligence artificielle dans la vie quotidienne.

Les bénévoles peuvent s’engager dans des interventions, contribuer à l’organisation d’événements, participer à des actions de communication ou à des activités de formation.

L’adhésion permet de soutenir les actions de l’association, de participer aux projets et événements, et de contribuer à la diffusion d’une intelligence artificielle responsable.

Il n'y a pas de conditions d'adhésion et pas de cotisation.
Génération IA accorde une importance particulière à l’intelligence artificielle responsable et éthique.

L’association sensibilise aux biais algorithmiques, à la protection des données, à la transparence des modèles, aux limites de l’intelligence artificielle, ainsi qu’à l’impact social et environnemental de l’IA.

L’objectif est de promouvoir une utilisation réfléchie, éthique et consciente de l’intelligence artificielle.

Il n’est pas nécessaire d’avoir des connaissances techniques pour participer aux activités de Génération IA.

Les adhérents et membres de Génération IA sont formés par nos équipes pour pouvoir à leurs tours donner des conférences et participer aux interventions.
Les informations pratiques et les contacts de Génération IA sont les suivants.

Adresse email : contact@generationia-asso.fr
Réseaux sociaux :
LinkedIn : Génération IA France
Instagram : generationia_france


Concernant les tarifs, il suffit de demander un devis en adressant un mail sur l'adresse de l'association.

Génération IA intervient partout en Europe et principalement en France.
A titre informatif, les membres du bureau de l'association sont : 
- Président de Génération IA France : Redouane Oumar NDIAYE
- Secrétaire Général : Rodrigue HOARAU
- Secrétaire Général Adjoint : Anis EL JELJAL
- Vice présidente Génération IA Occitanie : Inès HIJAZI
- Vice président Génération IA Ile-de-France : Sébastien DORS
- Secrétaire Génération IA Occitanie : Nesrine AYROUR

]
"""
messages = [  # conversation's list for memory
    {"role": "system", "content": system_prompt},
    {"role": "system", "content": f"Knowledge base :\n{knowledge_base}"},
]

print("GenBot est prêt ! Vous pouvez quitter la conversation en tapant exit.")

while True:
    user_input = input("Vous : ")

    if user_input.lower() == "exit":
        print("Bye !")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.complete(model=MODEL, messages=messages)

    bot_reply = response.choices[0].message.content
    print("GenBot :", bot_reply, "\n")

    messages.append({"role": "assistant", "content": bot_reply})
