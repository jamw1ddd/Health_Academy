from django.urls import path

from patient import views

app_name = "patient"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("appointments/", views.appointments, name="appointments"),
    path(
        "appointments/<appointment_id>/",
        views.appointment_detail,
        name="appointment_detail",
    ),
    path(
        "cancel-appointment/<appointment_id>/",
        views.cancel_appointment,
        name="cancel_appointment",
    ),
    path(
        "activate-appointment/<appointment_id>/",
        views.activate_appointment,
        name="activate_appointment",
    ),
    path(
        "complete-appointment/<appointment_id>/",
        views.complete_appointment,
        name="complete_appointment",
    ),
    path("payments/", views.payments, name="payments"),
    path("notifications/", views.notifications, name="notifications"),
    path("mark-as-read-notifications/<id>/", views.mark_as_read_notifications, name="mark_as_read_notifications"),
    path("profile/", views.profile, name="profile"),
]